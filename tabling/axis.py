"""Defines the `Axis` class."""

from typing import Iterator, List, Self
from .cell import Cell
from .element import Element


class Axis(Element):
    """Represents an axis of cells."""

    def __init__(self: Self, cellspacing: int = 0) -> None:
        super().__init__()
        self._cells: List[Cell] = []
        self.cellspacing: int = cellspacing

    def __len__(self: Self) -> int:
        return len(self._cells)

    def __iter__(self: Self) -> Iterator[Cell]:
        return iter(self._cells)

    def __getitem__(self: Self, index: int) -> Cell:
        try:
            return self._cells[index]
        except IndexError as exc:
            raise IndexError(f"Cell index {index} is out of range.") from exc

    def __contains__(self: Self, cell: Cell) -> bool:
        return cell in self._cells

    def add(self: Self, cell: Cell) -> None:
        """Adds a cell."""
        self._cells.append(cell)

    def insert(self: Self, index: int, cell: Cell) -> None:
        """Inserts a cell."""
        self._cells.insert(index, cell)

    def remove(self: Self, cell: Cell) -> None:
        """Removes a cell."""
        if cell not in self._cells:
            raise ValueError(f"Cell {cell} not found in this axis.")
        self._cells.remove(cell)

    def swap(self: Self, i: int, j: int) -> None:
        """Swaps cells."""
        self._cells[i], self._cells[j] = self._cells[j], self._cells[i]
