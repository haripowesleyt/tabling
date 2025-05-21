"""Defines the `Column` class."""

from copy import deepcopy
from typing import Self
from .axis import Axis


class Column(Axis):
    """Represents a table column."""

    def __str__(self: Self) -> str:
        if self.preserve:
            self = deepcopy(self)  # pylint: disable=self-cls-assignment
        self.normalize()
        return self._render(("\n" + "\n" * self.cellspacing).join(map(str, self._cells)))

    def normalize(self: Self) -> None:
        """Sets uniform, fixed spacing values to cells."""
        max_margin_left = max_margin_right = max_padding_left = max_padding_right = max_width = 0
        any_left_border = any_right_border = False
        for cell in self._cells:
            max_margin_left = max(max_margin_left, cell.margin.left)
            max_margin_right = max(max_margin_right, cell.margin.right)
            max_padding_left = max(max_padding_left, cell.padding.left)
            max_padding_right = max(max_padding_right, cell.padding.right)
            max_width = max(max_width, cell.width)
            any_left_border = any_left_border or bool(cell.border.left.style)
            any_right_border = any_right_border or bool(cell.border.right.style)
        for cell in self._cells:
            cell.margin.inline = max_margin_left, max_margin_right
            cell.padding.inline = max_padding_left, max_padding_right
            cell.width = max_width
            cell.font += self.font
            if any_left_border and not cell.border.left.style:
                cell.padding.left += 1
            if any_right_border and not cell.border.right.style:
                cell.padding.right += 1
