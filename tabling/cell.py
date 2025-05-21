"""Defines the `Cell` class."""

from typing import Any, Self
from printly import unstyle
from .element import Element
from .properties import Text


class Cell(Element):
    """Represents a table cell."""

    def __init__(self: Self, value: Any) -> None:
        super().__init__()
        self.text: Text = Text(value)
        self._width = self._height = -1

    def __str__(self: Self) -> str:
        text = self._rendered_text
        text = self.font.apply(text)
        return self._render(text)

    @property
    def value(self: Self) -> Any:
        """Gets the cell value."""
        return self.text.text

    @value.setter
    def value(self: Self, value: Any) -> None:
        self.text.text = value

    @property
    def width(self: Self) -> int:
        """Gets the cell width."""
        if self._width == -1:
            return max(map(len, map(unstyle, self._rendered_text.split("\n"))))
        return self._width

    @width.setter
    def width(self: Self, width: int) -> None:
        self._width = self._validate_measurement(width)

    @property
    def height(self: Self) -> int:
        """Gets the cell height."""
        if self._height == -1:
            return self._rendered_text.count("\n") + 1
        return self._height

    @height.setter
    def height(self: Self, height: int) -> None:
        self._height = self._validate_measurement(height)

    @property
    def _rendered_text(self: Self) -> str:
        return self.text.render(self._width, self._height)

    @staticmethod
    def _validate_measurement(measurement: int) -> int:
        if measurement < 0:
            raise ValueError(f"Invalid cell measurement {measurement}. Must be >= 0.")
        return measurement
