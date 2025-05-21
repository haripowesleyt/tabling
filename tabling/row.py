"""Defines the `Row` class."""

from typing import Self
from .axis import Axis


class Row(Axis):
    """Represents a table row."""

    def __str__(self: Self) -> str:
        """Generates a visual representation of the row."""
        self._normalize()
        cells_lines = tuple(s.split("\n") for s in map(str, self._cells))
        row_lines = [""] * max(map(len, cells_lines))
        number_of_cells = len(cells_lines)
        for cell_index, cell_lines in enumerate(cells_lines):
            for line_index, line in enumerate(cell_lines):
                if cell_index < number_of_cells:
                    line += " " * self.cellspacing
                row_lines[line_index] += line
        return self._render("\n".join(row_lines))

    def _normalize(self: Self) -> None:
        max_margin_top = max_margin_bottom = max_padding_top = max_padding_bottom = max_height = 0
        for cell in self._cells:
            max_margin_top = max(max_margin_top, cell.margin.top)
            max_margin_bottom = max(max_margin_bottom, cell.margin.bottom)
            max_padding_top = max(max_padding_top, cell.padding.top)
            max_padding_bottom = max(max_padding_bottom, cell.padding.bottom)
            max_height = max(max_height, cell.height)
        for cell in self._cells:
            cell.margin.block = max_margin_top, max_margin_bottom
            cell.padding.block = max_padding_top, max_padding_bottom
            cell.height = max_height
            cell.font += self.font
