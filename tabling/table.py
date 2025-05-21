"""Defines the `Table` class."""

import csv
import json
import re
from copy import deepcopy
from typing import Any, Dict, Iterable, Iterator, List, Optional, Self, Union
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

    def __len__(self: Self) -> int:
        return len(self._rows)

    def __iter__(self: Self) -> Iterator:
        return iter(self._rows)

    def __getitem__(self: Self, index: int) -> Row:
        try:
            return self._rows[index]
        except IndexError as exc:
            raise IndexError(f"Row index {index} is out of range.") from exc

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

    def replace(self: Self, value: Any, repl: Any) -> None:
        """Replaces matching values."""
        for row in self._rows:
            for cell in row:
                if re.findall(f"{value}", f"{cell.value}"):
                    cell.value = re.sub(f"{value}", repl, f"{cell.value}", 0, re.IGNORECASE)

    def clear(self: Self) -> None:
        """Removes all rows."""
        self._rows, self._columns = [], []

    def import_csv(self: Self, filepath: str) -> None:
        """Imports rows from csv file."""
        try:
            with open(filepath, "r", encoding="utf-8") as csv_file:
                for entries in csv.reader(csv_file):
                    self.add_row(entries)
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"CSV file {filepath!r} not found!") from exc

    def export_csv(self: Self, filepath: str) -> None:
        """Exports rows to csv file."""
        with open(filepath, "w", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            for row in self._rows:
                writer.writerow((f"{cell.value}" for cell in row))

    def import_json(  # pylint: disable=too-many-branches
        self: Self, filepath: str, key: Optional[str] = None
    ) -> None:
        """Imports rows from json file."""
        try:
            with open(filepath, "r", encoding="utf-8") as json_file:
                root = json.load(json_file)
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"JSON file {filepath} not found!") from exc
        while True:
            if isinstance(root, list):
                if all((isinstance(entries, list) for entries in root)):
                    for entries in root:
                        self.add_row(entries)
                elif all((isinstance(entries, dict) for entries in root)):
                    header: List[Any] = []
                    for obj in root:
                        if header != (keys := list(obj.keys())):
                            header += [k for k in keys if not k in header]
                    for obj in root:
                        for _key in header:
                            obj[_key] = obj.get(_key, "")
                    if header:
                        self.add_row(header)
                    for obj in root:
                        self.add_row((obj[key] for key in header))
                else:
                    raise ValueError("JSON array root should be of one type: array or object.")
            elif isinstance(root, dict):
                if key:
                    if root := root.get(key):
                        continue
                    raise KeyError(f"No key {key} in the root object.")
                raise ValueError("No key given for a json file with an object root.")
            break

    def export_json(
        self: Self, filepath: str, key: Optional[str] = None, as_objects: bool = True
    ) -> None:
        """Exports rows to json file."""
        contents: List[Union[Dict, List]] = []
        if as_objects:
            if self._rows:
                for row in self._rows[1:]:
                    contents.append({self._rows[0][i].value: row[i].value for i in range(len(row))})
        else:
            contents = [[cell.value for cell in row] for row in self._rows]
        with open(filepath, "w", encoding="utf-8") as json_file:
            json.dump({key: contents} if key else contents, json_file, indent=2)

    def export_txt(self: Self, filepath: str) -> None:
        """Exports plain, rendered table to plain/txt file."""
        with open(filepath, "w", encoding="utf-8") as txt_file:
            txt_file.write(unstyle(str(self)))

    def _get_row(self: Self, index: int) -> Row:
        if abs(index) > len(self._rows):
            raise IndexError(f"Row index {index} is out of range.")
        return self._rows[index]

    def _get_col(self: Self, index: int) -> Column:
        if abs(index) > len(self._columns):
            raise IndexError(f"Column index {index} is out of range.")
        return self._columns[index]
