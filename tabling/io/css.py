"""Defines the `css` class."""

import re
from typing import Dict, List, Optional, Sequence
from printly.const import RGB_DELIMITER, FS_DELEMITER
from printly.validate import validate_color, validate_font_style
from ..element import Element


class css:  # pylint: disable=invalid-name
    """Represents css io operations."""

    @staticmethod
    def make(element: Element, selector: str) -> str:
        """Makes CSS from an element's styles."""
        styles = ""
        if element.background.color:
            styles += f"      background-color: {element.background.color};\n"
        for side in ("left", "right", "top", "bottom"):
            border_side = getattr(element.border, side)
            if border_style := border_side.style:
                border_width = "1px"
                if border_style == "single":
                    border_style = "solid"
                elif border_style == "solid":
                    border_width = "2px"
                styles += f"      border-{side}-style: {border_style};\n"
                styles += f"      border-{side}-width: {border_width};\n"
            if border_side.color:
                styles += f"      border-{side}-color: {border_side.color};\n"
        if element.font.style:
            for font_style in validate_font_style(element.font.style).split(FS_DELEMITER):
                if font_style == "bold":
                    styles += "      font-weight: bold;\n"
                elif font_style == "italic":
                    styles += "      font-style: italic;\n"
                elif font_style == "strikethrough":
                    styles += "      text-decoration: line-through;\n"
                elif font_style == "underline":
                    styles += "      text-decoration: underline;\n"
                elif font_style == "overline":
                    styles += "      text-decoration: overline;\n"
                elif font_style == "double-underline":
                    styles += "      text-decoration: underline double;\n"
                elif font_style == "hidden":
                    styles += "      opacity: 0;\n"
        if element.font.color:
            if RGB_DELIMITER in (color := validate_color(element.font.color)):
                styles += "      color: rgb({color});\n"
            else:
                styles += f"      color: {color};\n"
        for side in ("left", "right", "top", "bottom"):
            if margin := getattr(element.margin, side):
                styles += f"      margin-{side}: {margin}ch;\n"
        for side in ("left", "right", "top", "bottom"):
            if padding := getattr(element.padding, side):
                styles += f"      padding-{side}: {padding}ch;\n"
        if hasattr(element, "text"):
            if element.text.justify != "left":
                styles += f"      text-align: {element.text.justify};\n"
            if not element.text.wrap:
                styles += "      white-space: nowrap;\n"
            if not element.text.visible:
                styles += "      opacity: 0;\n"
            if element.text.reverse:
                styles += "      text-direction: rtl;\n"
            if element.text.letter_spacing:
                styles += f"      letter-spacing: {element.text.letter_spacing};\n"
            if element.text.word_spacing != 1:
                styles += f"      word-spacing: {element.text.word_spacing};\n"
        if hasattr(element, "width"):
            if (width := element.width) != -1:
                styles += f"      width: {width}ch;\n"
        if hasattr(element, "height"):
            if (height := element.height) != -1:
                styles += f"      height: {height}rem;\n"
        if styles:
            return f"    {selector} {{\n" + styles + "    }\n"
        return ""

    @staticmethod
    def put(styles: Dict[str, str], element: Element) -> None:
        """Puts css styles on an element"""

        def check_color(values: List[str]) -> Optional[str]:
            for value in values:
                if "rgb" in value:
                    value = value.lstrip("rgb(").rstrip(")").strip()
                try:
                    color = validate_color(value)
                except ValueError:
                    pass
                else:
                    values.remove(value)
                    return color
            return None

        def check_border_width(values: List[str]) -> int:
            for value in values:
                if (first_digit := value[0:1]).isdigit():
                    values.remove(value)
                    return int(first_digit)
            return 1

        def check_border_style(values: List[str]) -> Optional[str]:
            width = check_border_width(values)
            supported = ("double", "dashed", "dotted", "solid")
            unsupported = ("none", "hidden", "groove", "ridge", "inset", "outset")
            for value in values:
                if value in supported:
                    if value == "solid" and width == 1:
                        return "single"
                    return value
                if value in unsupported:
                    if value in ("none", "hidden"):
                        return None
                    return "solid"
            return None

        if background := styles.get("background"):
            element.background.color = check_color([background])
        if background_color := styles.get("background-color"):
            element.background.color = check_color([background_color])
        if border := styles.get("border"):
            values = border.split()
            element.border.color = check_color(values)
            element.border.style = check_border_style(values)
        if border_style := styles.get("border-style"):
            element.border.style = check_border_style([border_style])
        if border_color := styles.get("border-color"):
            element.border.color = check_color([border_color])
        if border_width := styles.get("border-width"):
            width = check_border_width([border_width])
            if element.border.style == "single" and width > 1:
                element.border.style = "solid"
        for side in ("left", "right", "top", "bottom"):
            border_side = getattr(element.border, side)
            if borderside := styles.get(f"border-{side}"):
                values = borderside.split()
                border_side.color = check_color(values)
                border_side.style = check_border_style(values)
            if border_style := styles.get(f"border-{side}-style"):
                border_side.style = check_border_style([border_style])
            if border_color := styles.get(f"border-{side}-color"):
                border_side.color = check_color([border_color])
            if border_width := styles.get(f"border-{side}-width"):
                width = check_border_width([border_width])
                if border_side.style == "single" and width > 1:
                    border_side.style = "solid"
            if margin_side := styles.get(f"margin-{side}"):
                if margin_side.isdigit():
                    setattr(element.margin, side, int(margin_side))
            if padding_side := styles.get(f"padding-{side}"):
                if padding_side.isdigit():
                    setattr(element.padding, side, int(padding_side))
        for side in ("inline", "block"):
            if margin_side := styles.get(f"margin-{side}"):
                if margin_side.isdigit():
                    setattr(element.margin, side, (int(margin_side),) * 2)
            if padding_side := styles.get(f"padding-{side}"):
                if padding_side.isdigit():
                    setattr(element.padding, side, (int(padding_side),) * 2)
        if margin := styles.get("margin"):
            margins: Sequence = margin.split()
            if all((m.isdigit() for m in margins)):
                margins = tuple(map(int, margins))
                if len(margins) == 1:
                    element.margin.all = margins * 4
                elif len(margins) == 2:
                    element.margin.block = (margins[0],) * 2
                    element.margin.inline = (margins[1],) * 2
                elif len(margins) == 4:
                    element.margin.top = margins[0]
                    element.margin.right = margins[1]
                    element.margin.bottom = margins[2]
                    element.margin.left = margins[3]
        if padding := styles.get("padding"):
            paddings: Sequence = padding.split()
            if all((m.isdigit() for m in paddings)):
                paddings = tuple(map(int, paddings))
                if len(paddings) == 1:
                    element.padding.all = paddings * 4
                elif len(paddings) == 2:
                    element.padding.block = (paddings[0],) * 2
                    element.padding.inline = (paddings[1],) * 2
                elif len(paddings) == 4:
                    element.padding.top = paddings[0]
                    element.padding.right = paddings[1]
                    element.padding.bottom = paddings[2]
                    element.padding.left = paddings[3]
        if color := styles.get("color"):
            element.font.color = check_color([color])
        font_styles = []
        if font_weight := styles.get("font-weight"):
            if font_weight.startswith("bold") or font_weight in map(str, range(400, 900, 100)):
                font_styles.append("bold")
        if font_style := styles.get("font-style"):
            if font_style in ("bold", "italic", "oblique"):
                if font_style == "oblique":
                    font_style = "italic"
                font_styles.append(font_style)
        if text_decoration := styles.get("text-decoration"):
            for decoration in text_decoration.split():
                if decoration in ("line-through", "underline", "overline", "double"):
                    if decoration == "line-through":
                        decoration = "strikethrough"
                    elif decoration == "double":
                        decoration = "double-underline"
                    font_styles.append(decoration)
        if opacity := styles.get("opacity"):
            if opacity.isdigit():
                if int(opacity) == 0:
                    font_styles.append("hidden")
        element.font.style = "+".join(font_styles)
        if hasattr(element, "text"):
            if text_align := styles.get("text-align"):
                if text_align in ("left", "center", "right"):
                    element.text.justify = text_align
            if white_space := styles.get("white-space"):
                element.text.wrap = white_space != "nowrap"
            if text_direction := styles.get("text-direction"):
                element.text.reverse = text_direction == "rtl"
            if letter_spacing := styles.get("letter-spacing"):
                if letter_spacing.isdigit():
                    element.text.letter_spacing = int(letter_spacing)
            if word_spacing := styles.get("word-spacing"):
                if word_spacing.isdigit():
                    element.text.word_spacing = int(word_spacing)
        if hasattr(element, "width"):
            if width := styles.get("width"):  # type: ignore
                if matcth := re.search(r"(?P<width>\d+)\w+", width):
                    element.width = int(matcth["width"])
        if hasattr(element, "height"):
            if height := styles.get("height"):  # type: ignore
                if matcth := re.search(r"(?P<height>\d+)\w+", height):
                    element.height = int(matcth["height"])
