"""Defines the `Table` class."""

import re
from copy import deepcopy
from typing import Any, Iterable, Iterator, List, Self, Union
from printly import unstyle
from .cell import Cell
from .column import Column
from .element import Element
from .properties import Background
from .row import Row


class Table(Element):
    """Represents a table."""

    def __init__(self: Self, colspacing: int = 1, rowspacing: int = 0) -> None:
        super().__init__()
        self._rows: List[Row] = []
        self._columns: List[Column] = []
        self.colspacing: int = colspacing
        self.rowspacing: int = rowspacing

    def __bool__(self: Self) -> bool:
        return bool(self._rows)

    def __len__(self: Self) -> int:
        return len(self._rows)

    def __iter__(self: Self) -> Iterator:
        return iter(self._rows)

    def __getitem__(self: Self, index: Union[int, slice]):
        if isinstance(index, slice):
            return self._rows[index.start or 0 : index.stop or len(self._rows) : index.step or 1]
        try:
            return self._rows[index]
        except IndexError as exc:
            raise IndexError(f"Row index {index} is out of range.") from exc

    def __add__(self: Self, other: "Table") -> "Table":
        other_columns = len(other[0])
        self_columns = len(self._columns)
        if (diff := other_columns - self_columns) > 0:
            for _ in range(diff):
                self.add_column("")
        elif diff < 0:
            for _ in range(abs(diff)):
                other.add_column("")
        for row in other:
            self._rows.append(row)
            for index, cell in enumerate(row):
                self._columns[index].add(cell)
        return self

    def __str__(self: Self) -> str:
        if self.preserve:
            self = deepcopy(self)  # pylint: disable=self-cls-assignment
        for column in self._columns:
            column.normalize()
        any_left_border = any_right_border = False
        for row in self._rows:
            any_left_border = any_left_border or bool(row.border.left.style)
            any_right_border = any_right_border or bool(row.border.right.style)
        for row in self._rows:
            row.font += self.font
            row.cellspacing = max(row.cellspacing, self.colspacing)
            if any_left_border and not row.border.left.style:
                row.padding.left += 1
            if any_right_border and not row.border.right.style:
                row.padding.right += 1
            row.preserve = False
        return self._render(("\n" + "\n" * self.rowspacing).join(map(str, self._rows)))

    def add_row(self: Self, entries: Iterable[Any]) -> None:
        """Adds a row."""
        self.insert_row(len(self._rows), entries)

    def add_column(self: Self, entries: Iterable[Any]) -> None:
        """Adds a column."""
        self.insert_column(len(self._columns), entries)

    def insert_row(self: Self, index: int, entries: Iterable[Any]) -> None:
        """Inserts a row."""
        entries = list(entries)
        len_entries, len_columns = len(entries), len(self._columns)
        if len_entries < len_columns:
            entries += [""] * (len_columns - len_entries)
        elif len_entries > len_columns:
            for _ in range(len_entries - len_columns):
                self._columns.append(column := Column())
                for row in self._rows:
                    row.add(cell := Cell(""))
                    column.add(cell)
        row = Row()
        for cell in map(Cell, entries):
            row.add(cell)
        self._rows.insert(index, row)
        for column_index, cell in enumerate(row):
            self._columns[column_index].insert(index, cell)

    def insert_column(self: Self, index: int, entries: Iterable[Any]) -> None:
        """Inserts a column."""
        entries = list(entries)
        len_entries, len_rows = len(entries), len(self._rows)
        if len_entries < len_rows:
            entries += [""] * (len_rows - len_entries)
        elif len_entries > len_rows:
            for _ in range(len_entries - len_rows):
                self._rows.append(row := Row())
                for column in self._columns:
                    column.add(cell := Cell(""))
                    row.add(cell)
        column = Column()
        for cell in map(Cell, entries):
            column.add(cell)
        self._columns.insert(index, column)
        for row_index, cell in enumerate(column):
            self._rows[row_index].insert(index, cell)

    def remove_row(self: Self, index: int) -> None:
        """Removes a row."""
        row = self._get_row(index)
        for column_index, cell in enumerate(row):
            self._columns[column_index].remove(cell)
        self._rows.remove(row)

    def remove_column(self: Self, index: int) -> None:
        """Removes a column."""
        column = self._get_col(index)
        for row_index, cell in enumerate(column):
            self._rows[row_index].remove(cell)
        self._columns.remove(column)

    def swap_rows(self: Self, index1: int, index2: int) -> None:
        """Swaps rows."""
        self._rows[index1], self._rows[index2] = self._get_row(index2), self._get_row(index1)
        for column in self._columns:
            column.swap(index1, index2)

    def swap_columns(self: Self, index1: int, index2: int) -> None:
        """Swaps columns."""
        self._columns[index1], self._columns[index2] = self._get_col(index2), self._get_col(index1)
        for row in self._rows:
            row.swap(index1, index2)

    def sort_rows(self: Self, key: int, start: int = 0, reverse: bool = False) -> None:
        """Sorts rows by a given key column."""
        for index, row in enumerate(
            sorted(self._rows[start:], key=lambda row: f"{row[key].value}", reverse=reverse),
            start=start,
        ):
            self.swap_rows(index1=index, index2=self._rows.index(row))

    def sort_columns(self: Self, key: int, start: int = 0, reverse: bool = False) -> None:
        """Sorts columns by a given key row."""
        for index, column in enumerate(
            sorted(self._columns, key=lambda column: f"{column[key].value}", reverse=reverse),
            start=start,
        ):
            self.swap_columns(index1=index, index2=self._columns.index(column))

    def find(self: Self, value: Any) -> None:
        """Displays a table highlighting matches."""
        repl = Background(color="yellowgreen").apply(f"{value}")
        print(self._render(re.sub(f"{value}", repl, unstyle(str(self)), re.IGNORECASE)))

    def replace(self: Self, old: Any, new: Any) -> None:
        """Replaces matching values."""
        for row in self._rows:
            for cell in row:
                if re.findall(f"{old}", f"{cell.value}"):
                    cell.value = re.sub(f"{old}", new, f"{cell.value}", 0, re.IGNORECASE)

    def clear(self: Self) -> None:
        """Removes all rows."""
        self._rows, self._columns = [], []

    def _get_row(self: Self, index: int) -> Row:
        if abs(index) > len(self._rows):
            raise IndexError(f"Row index {index} is out of range.")
        return self._rows[index]

    def _get_col(self: Self, index: int) -> Column:
        if abs(index) > len(self._columns):
            raise IndexError(f"Column index {index} is out of range.")
        return self._columns[index]
