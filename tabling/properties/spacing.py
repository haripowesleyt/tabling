"""Defines the `Spacing` class."""

from typing import Self, Tuple
from printly import unstyle


class Spacing:  # pylint: disable=too-many-instance-attributes
    """Represents inner or outer spacing of an element."""

    def __init__(self: Self, left: int, right: int, top: int, bottom: int) -> None:
        self.left: int = left
        self.right: int = right
        self.top: int = top
        self.bottom: int = bottom

    def apply(self: Self, text: str) -> str:
        """Applies the spacing to given text."""
        return self._apply_inline(self._apply_block(text))

    def _apply_inline(self: Self, text: str) -> str:
        left, right = " " * self.left, " " * self.right
        return "\n".join(left + line + right for line in text.split("\n"))

    def _apply_block(self: Self, text: str) -> str:
        length = max(map(len, map(unstyle, text.split("\n"))))
        top = (" " * length + "\n") * self.top
        bottom = ("\n" + " " * length) * self.bottom
        return top + text + bottom

    @staticmethod
    def _validate(value: int) -> int:
        if value < 0:
            raise ValueError(f"Invalid spacing value {value}. Must be >= 0.")
        return value

    @classmethod
    def _validate_pair(cls, values: Tuple[int, int]) -> Tuple[int, int]:
        if len(values) != 2:
            raise ValueError(f"Invalid spacing pair values {values}. Must be a 2-int tuple.")
        return cls._validate(values[0]), cls._validate(values[1])

    @property
    def left(self: Self) -> int:
        """Gets the spacing to the left."""
        return self._left

    @left.setter
    def left(self: Self, left: int) -> None:
        self._left = self._validate(left)

    @property
    def right(self: Self) -> int:
        """Gets the spacing to the right."""
        return self._right

    @right.setter
    def right(self: Self, right: int) -> None:
        self._right = self._validate(right)

    @property
    def top(self: Self) -> int:
        """Gets the spacing to the top."""
        return self._top

    @top.setter
    def top(self: Self, top: int) -> None:
        self._top = self._validate(top)

    @property
    def bottom(self: Self) -> int:
        """Gets the spacing to the bottom."""
        return self._bottom

    @bottom.setter
    def bottom(self: Self, bottom: int) -> None:
        self._bottom = self._validate(bottom)

    @property
    def inline(self: Self) -> Tuple[int, int]:
        """Gets the spacing to the left and right."""
        return self.left, self.right

    @inline.setter
    def inline(self: Self, values: Tuple[int, int]) -> None:
        self.left, self.right = self._validate_pair(values)

    @property
    def block(self: Self) -> Tuple[int, int]:
        """Gets the spacing to the top and bottom."""
        return self.left, self.right

    @block.setter
    def block(self: Self, values: Tuple[int, int]) -> None:
        self.top, self.bottom = self._validate_pair(values)

    @property
    def all(self: Self) -> Tuple[int, int, int, int]:
        """Gets the padding to the left, right, top, and bottom respectively."""
        return self.left, self.right, self.top, self.bottom

    @all.setter
    def all(self: Self, values: Tuple[int, int, int, int]):
        if len(values) != 4:
            raise ValueError(f"Invalid spacing values {values}. Expected a 4-int tuple.")
        self.left, self.right, self.top, self.bottom = map(self._validate, values)
