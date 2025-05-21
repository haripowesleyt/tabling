"""Defines the `Font` class."""

from typing import Optional, Self
from printly import style as apply_font
from printly.types import Color, FontStyle as Style


class Font:
    """Represents the font of an element."""

    def __init__(self: Self, style: Optional[Style], color: Optional[Color]) -> None:
        self.style: Optional[Style] = style
        self.color: Optional[Color] = color

    def __add__(self: Self, other: "Font") -> "Font":
        if self.style and other.style:
            style: Optional[str] = "+".join(set(self.style.split("+") + other.style.split("+")))
        else:
            style = self.style or other.style
        return Font(style, self.color or other.color)

    def apply(self: Self, text: str) -> str:
        """Applies the font to given text."""
        return apply_font(text, fg=self.color, fs=self.style)
