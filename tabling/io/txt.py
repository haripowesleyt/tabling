"""Defines the `txt` class."""

from printly import unstyle
from ..table import Table


class txt:  # pylint: disable=invalid-name, too-few-public-methods
    """Represents TXT io operations."""

    @staticmethod
    def dump(table: Table, filepath: str) -> None:
        """Dumps table rows to TXT file."""
        preserve = table.preserve
        table.preserve = True
        with open(filepath, "w", encoding="utf-8") as txt_file:
            txt_file.write(unstyle(str(table)))
        table.preserve = preserve
