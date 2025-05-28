"""Define the `json` class."""

from json import dump as jdump, load as jload
from typing import Any, Dict, List, Optional, Union
from ..table import Table


class json:  # pylint: disable=invalid-name
    """Represents JSON io operations."""

    @staticmethod
    def dump(
        table: Table, filepath: str, key: Optional[str] = None, as_objects: bool = True
    ) -> None:
        """Dumps a table into a JSON file."""
        rows: List[Union[Dict, List]] = []
        if as_objects:
            try:
                header = table[0]
            except IndexError:
                pass
            else:
                for row in table[1:]:
                    rows.append({header[i].value: row[i].value for i in range(len(table))})
        else:
            rows = [[cell.value for cell in row] for row in table]
        with open(filepath, "w", encoding="utf-8") as json_file:
            jdump({key: rows} if key else rows, json_file, indent=2)

    @staticmethod
    def load(  # pylint: disable=too-many-branches
        table: Table, filepath: str, key: Optional[str] = None
    ):
        """Loads rows from JSON file to table."""
        try:
            with open(filepath, "r", encoding="utf-8") as json_file:
                root = jload(json_file)
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"JSON file {filepath} not found!") from exc
        while True:
            if isinstance(root, list):
                if all((isinstance(row, list) for row in root)):
                    for row in root:
                        table.add_row(row)
                elif all((isinstance(row, dict) for row in root)):
                    header: List[Any] = []
                    for obj in root:
                        if header != (keys := list(obj.keys())):
                            header += [k for k in keys if not k in header]
                    for obj in root:
                        for key_ in header:
                            obj[key_] = obj.get(key_, "")
                    if header:
                        table.add_row(header)
                    for obj in root:
                        table.add_row((obj[key] for key in header))
                else:
                    raise ValueError("All JSON rows should be of same type: array or object.")
            elif isinstance(root, dict):
                if key:
                    if root := root.get(key):
                        continue
                    raise KeyError(f"No key {key} in JSON file root.")
                raise ValueError("No key given for JSON file object root.")
            break
