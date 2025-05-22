"""Defines the `Element` class."""

from typing import Self
from .properties import Background, Border, Font, Margin, Padding


class Element:  # pylint: disable=too-few-public-methods
    """Represents a table element."""

    def __init__(self: Self) -> None:
        self.background: Background = Background(color=None)
        self.border: Border = Border(style=None, color=None)
        self.font: Font = Font(style=None, color=None)
        self.margin: Margin = Margin(left=0, right=0, top=0, bottom=0)
        self.padding: Padding = Padding(left=0, right=0, top=0, bottom=0)
        self.preserve: bool = True

    def _render(self: Self, text: str) -> str:
        """Generates a visual representation of the element."""
        text = self.padding.apply(text)
        text = self.background.apply(text)
        text = self.border.apply(text)
        return self.margin.apply(text)
