"""Defines the html class."""

import re
from typing import Dict, Iterator, List, Tuple
from .css import css
from ..table import Table


class html:  # pylint: disable=invalid-name, too-few-public-methods
    """Represents html file io."""

    @staticmethod
    def dump(table: Table, filepath: str) -> None:  # pylint: disable=too-many-statements
        """Dumps a table into an html file."""
        page = (
            "<!DOCTYPE html>\n"
            + "<html>\n"
            + "<head>\n"
            + "  <title>Dumped Table</title>\n"
            + "  <style>\n"
        )
        page += css.make(table, ".table")
        for row_index, row in enumerate(table):
            page += css.make(row, f".row{-row_index}")
        for row_index, row in enumerate(table):
            for cell_index, cell in enumerate(row):
                page += css.make(cell, f".cell-{row_index}-{cell_index}")
        page += "  </style>\n"
        page += "</head>\n"
        page += "<body>\n"
        page += f'  <table cellspacing={table.colspacing} class="table">\n'
        for row_index, row in enumerate(table):
            page += f'    <tr class="row-{row_index}">\n'
            for cell_index, cell in enumerate(row):
                page += f'      <td class="cell-{row_index}-{cell_index}">{cell.value}</td>\n'
            page += "    </tr>\n"
        page += "  </table>\n"
        page += "<body>\n"
        page += "</html>\n"

        with open(filepath, "w", encoding="utf-8") as html_file:
            html_file.write(page)

    @staticmethod
    def load(table: Table, filepath: str, index: int = 0) -> None:
        """Loads rows from HTML file to table."""
        if tables := tuple(html.loadall(filepath)):
            table += tables[min(len(tables) - 1, index)]

    @staticmethod
    def loadall(filepath: str) -> Iterator[Table]:  # pylint: disable=too-many-locals
        """Loads all tables in an HTML file."""
        with open(filepath, "r", encoding="utf-8") as html_file:
            page = html_file.read()

        def findall(tag: str, scope: str) -> List[Tuple[str, str]]:
            return re.findall(rf"<{tag}(.*?)>(.*?)</{tag}>", scope, re.IGNORECASE | re.DOTALL)

        internal_css = "".join((s[1] for s in findall("style", page)))

        def get_styles(attrs: str) -> Dict[str, str]:
            styles: Dict[str, str] = {}

            def strip(text: str) -> str:
                text = re.sub(r"\s*;\s*", ";", text)
                text = re.sub(r"\s*:\s*", ":", text)
                text = re.sub(r'"', "", text)
                text = re.sub("\n", " ", text)
                return re.sub(r"\s{2,}", " ", text)

            attrs = strip(attrs).strip()
            for attr in sorted(attrs.split(), reverse=True):
                attr_name, attr_value = attr.strip().split("=")
                if attr_name in ("style", "class", "id"):
                    if attr_name in ("class", "id"):
                        attr_value = (r"\." if attr_name == "class" else "#") + attr_value
                        pattern = rf"{attr_value}\s*{{(.*?)}}"
                        attr_value = "".join(
                            re.findall(pattern, internal_css, re.IGNORECASE | re.DOTALL)
                        )
                    attr_value = strip(attr_value).strip().rstrip(";").lower()
                    if attr_value:
                        for style in sorted(attr_value.split(";")):
                            css_property, css_value = style.split(":")
                            styles[css_property.strip()] = css_value.strip()
            return styles

        for table_attrs, table in findall("table", page):
            tabling_table = Table()
            css.put(get_styles(table_attrs), tabling_table)
            for row_attrs, row in findall("tr", table):
                row = re.sub("(?:\\s{2,}|\n)", "", row)
                attrs_and_cells = findall("th", row) + findall("td", row)
                cell_attrs = tuple(t[0] for t in attrs_and_cells)
                cells = (t[1] for t in attrs_and_cells)
                cells = (re.sub(r"(?:\s{2,}|<.*?>|</.*?>)", "", c).strip() for c in cells)
                tabling_table.add_row(cells)
                css.put(get_styles(row_attrs), tabling_table[-1])
                for index, cell in enumerate(tabling_table[-1]):
                    css.put(get_styles(cell_attrs[index]), cell)
            yield tabling_table
