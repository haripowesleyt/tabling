"""Defines the `sqlite` class."""

from sqlite3 import connect
from typing import Self
from ..row import Row
from ..table import Table


class sqlite:
    """Represents sqlite io operations."""

    @staticmethod
    def dump(table: Table, filepath: str, title: str) -> None:
        """Dumps a table to sql file."""
        con = connect(filepath)
        if table:

            def get_values(row: Row) -> str:
                return str(tuple(f"{cell.value}" for cell in row))

            cur = con.cursor()
            cur.execute(f"CREATE TABLE {title} {get_values(table[0])};")
            for row in table[1:]:
                cur.execute(f"INSERT INTO {title} VALUES {get_values(row)};")
            con.commit()
        con.close()

    @staticmethod
    def load(table: Table, filepath: str, title: str) -> None:
        """Loads a table from sql file."""
        con = connect(filepath)
        cur = con.cursor()
        cur.execute(f"PRAGMA table_info({title});")
        table.add_row((col[1] for col in cur.fetchall()))
        cur.execute(f"SELECT * FROM {title};")
        for row in cur.fetchall():
            table.add_row(row)
        con.close()
