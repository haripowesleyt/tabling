"""Defines the `Text` class."""

from textwrap import fill
from typing import Any, Literal, Self, TypeAlias, Union, get_args
from printly import unstyle

Alignment: TypeAlias = Union[str, Literal["top", "center", "bottom"]]
Justification: TypeAlias = Union[str, Literal["left", "center", "right"]]


class Text:  # pylint: disable=too-many-instance-attributes, too-few-public-methods
    """Represents the text in a table cell."""

    def __init__(  # pylint: disable=too-many-arguments
        self: Self,
        text: Any,
        justify: Justification = "left",
        align: Alignment = "top",
        wrap: bool = True,
        visible: bool = True,
        reverse: bool = False,
        letter_spacing: int = 0,
        word_spacing: int = 1,
    ) -> None:
        self.text: Any = text
        self.justify: Justification = justify
        self.align: Alignment = align
        self.wrap: bool = wrap
        self.visible: bool = visible
        self.reverse: bool = reverse
        self.letter_spacing: int = letter_spacing
        self.word_spacing: int = word_spacing

    def render(self: Self, width: int, height: int) -> str:  # pylint: disable=too-many-branches
        """Generates a visual representation of the text."""
        text = unstyle(self.text)
        if self.reverse:
            text = text[::-1]
        words = ((" " * self.letter_spacing).join(words) for words in text.split())
        text = (" " * self.word_spacing).join(words)
        if width != -1:
            if self.wrap and width > 0:
                text = fill(text, width, replace_whitespace=False)
            else:
                text = text[:width]
            if self.justify == "left":
                justify = str.ljust
            elif self.justify == "center":
                justify = str.center
            elif self.justify == "right":
                justify = str.rjust
            else:
                raise ValueError(
                    f"Invalid text justification {self.justify!r}."
                    f"Expected one of {get_args(Justification)}"
                )
            text = "\n".join(map(lambda line: justify(line, width), text.split("\n")))
        if height != -1:
            if height < (lines := text.count("\n") + 1):
                text = "\n".join(text.split("\n")[:height])
            else:
                diff = height - lines
                if self.align == "top":
                    text += "\n" * diff
                elif self.align == "center":
                    text = "\n" * (diff // 2) + text + "\n" * (diff - (diff // 2))
                elif self.align == "bottom":
                    text = "\n" * diff + text
                else:
                    raise ValueError(
                        f"Invalid text vertical alignment {self.align}."
                        f"Expected one of {get_args(Alignment)}"
                    )
        if not self.visible:
            for char in text:
                text = text.replace(char, " ") if char != "\n" else text

        max_width = max(map(len, (text_lines := text.split("\n"))))
        return "\n".join((line.ljust(max_width) for line in text_lines))
