"""Defines the `Background` class."""

from typing import Optional, Self
from printly import style as apply_color
from printly.types import Color


class Background:  # pylint: disable=too-few-public-methods
    """Represents the background of an element."""

    def __init__(self: Self, color: Optional[Color]) -> None:
        self.color: Optional[Color] = color

    def apply(self: Self, text: str) -> str:
        """Applies the background to given text."""
        return apply_color(text, bg=self.color)
