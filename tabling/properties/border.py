"""Defines the `Border` class."""

from typing import Dict, Literal, Optional, Self, TypeAlias, Union
from printly import style as apply_color, unstyle
from printly.types import Color

Style: TypeAlias = Union[str, Literal["single", "double", "dashed", "dotted", "solid", "curved"]]
Side: TypeAlias = Literal[
    "left", "right", "top", "bottom", "top-left", "top-right", "bottom-left", "bottom-right"
]


class Border:  # pylint: disable=too-many-instance-attributes
    """Represents a border."""

    def __init__(self: Self, style: Optional[Style], color: Optional[Color]) -> None:
        self.left = self._Side("left", style, color)
        self.right = self._Side("right", style, color)
        self.top = self._Side("top", style, color)
        self.bottom = self._Side("bottom", style, color)
        self.style: Optional[Style] = style
        self.color: Optional[Color] = color

    def apply(self: Self, text: str) -> str:
        """Applies the border to given text."""
        left, right = self.left.render(1), self.right.render(1)
        length = max(map(len, map(unstyle, text.split("\n"))))
        inline = "\n".join(
            left + line.ljust(length + len(line) - len(unstyle(line))) + right
            for line in text.split("\n")
        )
        overline = underline = ""
        if self.top.char:
            top_left = self._Side("top-left", self.left.style, self.left.color)
            top_right = self._Side("top-right", self.right.style, self.right.color)
            top_left.char = top_left.char or self.left.char
            top_right.char = top_right.char or self.right.char
            overline = top_left.render(1) + self.top.render(length) + top_right.render(1) + "\n"
        if self.bottom.char:
            bottom_left = self._Side("bottom-left", self.left.style, self.left.color)
            bottom_right = self._Side("bottom-right", self.right.style, self.right.color)
            bottom_left.char = bottom_left.char or self.left.char
            bottom_right.char = bottom_right.char or self.right.char
            underline = "\n" + (
                bottom_left.render(1) + self.bottom.render(length) + bottom_right.render(1)
            )
        return overline + inline + underline

    @property
    def style(self: Self) -> Optional[Style]:
        """Gets the border style."""
        return self._style  # type: ignore

    @style.setter
    def style(self: Self, style: Optional[Style]) -> None:
        self.left.style = self.right.style = self.top.style = self.bottom.style = style
        self._style = style

    @property
    def color(self: Self) -> Optional[Color]:
        """Gets the border color."""
        return self._color

    @color.setter
    def color(self: Self, color: Optional[Color]) -> None:
        self.left.color = self.right.color = self.top.color = self.bottom.color = color
        self._color = color

    class _Side:

        def __init__(
            self: Self, side: Side, style: Optional[Style], color: Optional[Color]
        ) -> None:
            self._side: Side = side
            self.style: Optional[Style] = style
            self.color: Optional[Color] = color
            self.char: str

        def render(self: Self, length: int) -> str:
            """Generates a visual representation of the side."""
            return apply_color(self.char[0:1] * length, fg=self.color)

        @property
        def style(self: Self) -> Optional[Style]:
            """Gets the border style."""
            return self._style

        @style.setter
        def style(self: Self, style: Optional[Style]) -> None:
            if style not in (styles := tuple(self.CHARS)):
                raise ValueError(f"Invalid border style {style!r}. Expected one of {styles}.")
            self._style = style
            self.char = self.CHARS[self.style][self._side]

        CHARS: Dict[Optional[Style], Dict[Side, str]] = {
            None: {
                "left": "",
                "right": "",
                "top": "",
                "bottom": "",
                "top-left": "",
                "top-right": "",
                "bottom-left": "",
                "bottom-right": "",
            },
            "single": {
                "left": "│",
                "right": "│",
                "top": "─",
                "bottom": "─",
                "top-left": "┌",
                "top-right": "┐",
                "bottom-left": "└",
                "bottom-right": "┘",
            },
            "double": {
                "left": "║",
                "right": "║",
                "top": "═",
                "bottom": "═",
                "top-left": "╔",
                "top-right": "╗",
                "bottom-left": "╚",
                "bottom-right": "╝",
            },
            "dashed": {
                "left": "┊",
                "right": "┊",
                "top": "╌",
                "bottom": "╌",
                "top-left": "┌",
                "top-right": "┐",
                "bottom-left": "└",
                "bottom-right": "┘",
            },
            "dotted": {
                "left": "⸳",
                "right": "⸳",
                "top": "⸳",
                "bottom": "⸳",
                "top-left": "⸳",
                "top-right": "⸳",
                "bottom-left": "⸳",
                "bottom-right": "⸳",
            },
            "solid": {
                "left": "┃",
                "right": "┃",
                "top": "━",
                "bottom": "━",
                "top-left": "┏",
                "top-right": "┓",
                "bottom-left": "┗",
                "bottom-right": "┛",
            },
            "curved": {
                "left": "│",
                "right": "│",
                "top": "─",
                "bottom": "─",
                "top-left": "╭",
                "top-right": "╮",
                "bottom-left": "╰",
                "bottom-right": "╯",
            },
            "single-double": {
                "left": "║",
                "right": "║",
                "top": "─",
                "bottom": "─",
                "top-left": "╓",
                "top-right": "╖",
                "bottom-left": "╙",
                "bottom-right": "╜",
            },
        }
