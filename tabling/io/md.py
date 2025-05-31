"""Defines the `md` class."""

from re import findall
from typing import Iterator, List
from ..cell import Cell
from ..row import Row
from ..table import Table


class md:  # pylint: disable=invalid-name, too-few-public-methods
    """Represents markdown io operations."""

    @staticmethod
    def dump(table: Table, filepath: str, has_header: bool) -> None:
        """Dumps table rows to markdown file."""

        if not table:
            return None

        def make_row(value: str, columns: int) -> Row:
            row = Row()
            for _ in range(columns):
                row.add(Cell(value))
            return row

        def row_to_md(row: Row, widths: List[int], fillchar: str = " ") -> str:
            md_row = "|"
            for index, cell in enumerate(row):
                md_row += f"{cell.value}".ljust(widths[index], fillchar) + "|"
            return md_row + "\n"

        number_of_columns = len(table[0])
        column_widths: List[int] = [0] * number_of_columns
        for row in table:
            for index, cell in enumerate(row):
                column_widths[index] = max(column_widths[index], cell.width)
        markdown = ""
        if has_header:
            markdown += row_to_md(table[0], column_widths)
        else:
            markdown += row_to_md(make_row("", number_of_columns), column_widths)
        markdown += row_to_md(make_row("-", number_of_columns), column_widths, "-")
        for row in table[int(has_header) :]:
            markdown += row_to_md(row, column_widths)
        with open(filepath, "w", encoding="utf-8") as md_file:
            md_file.write(markdown)

    @staticmethod
    def load(table: Table, filepath: str, index: int = 0) -> None:
        """Loads rows from MD file to table."""
        if tables := tuple(md.loadall(filepath)):
            table += tables[min(len(tables) - 1, index)]

    @staticmethod
    def loadall(filepath: str) -> Iterator[Table]:
        """Gets all tables in an MD file."""
        with open(filepath, "r", encoding="utf-8") as md_file:
            markdown = md_file.read()
        row_re = r"\s*\|(.*\|\s*)+" + "\n"
        table_re = f"({row_re}{row_re}(?:{row_re})*)"
        md_tables = tuple(m[0].strip() for m in findall(table_re, markdown))
        for table in md_tables:
            rows = [r.strip().strip("|") for r in table.split("\n")]
            del rows[1]
            table = Table()
            for row in rows:
                table.add_row((e.strip() for e in row.split("|")))
            yield table
