"""Defines the `tsv` class."""

from csv import reader, writer
from ..table import Table


class tsv:  # pylint: disable=invalid-name
    """Represents TSV io operations."""

    @staticmethod
    def dump(table: Table, filepath: str) -> None:
        """Dumps a table to a TSV file."""
        with open(filepath, "w", encoding="utf-8", newline="") as tsv_file:
            tsv_writer = writer(tsv_file, delimiter="\t")
            for row in table:
                tsv_writer.writerow((f"{cell.value}" for cell in row))

    @staticmethod
    def load(table: Table, filepath: str) -> None:
        """Loads rows from a TSV file to a table."""
        with open(filepath, "r", encoding="utf-8", newline="") as tsv_file:
            for entries in reader(tsv_file, delimiter="\t"):
                table.add_row(entries)
