"""Defines the `csv` class."""

from csv import reader, writer
from ..table import Table


class csv:  # pylint: disable=invalid-name
    """Represents CSV io operations."""

    @staticmethod
    def dump(table: Table, filepath: str) -> None:
        """Dumps a table to a CSV file."""
        with open(filepath, "w", encoding="utf-8") as csv_file:
            csv_writer = writer(csv_file)
            for row in table:
                csv_writer.writerow((f"{cell.value}" for cell in row))

    @staticmethod
    def load(table: Table, filepath: str) -> None:
        """Loads rows from a CSV file to a table."""
        with open(filepath, "r", encoding="utf-8") as csv_file:
            for entries in reader(csv_file):
                table.add_row(entries)
