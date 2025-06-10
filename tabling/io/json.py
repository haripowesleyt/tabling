"""Define the `json` class."""

from json import dump, load
from typing import Any, Dict, List, Optional, Union
from ..table import Table


class json:  # pylint: disable=invalid-name
    """Represents JSON io operations."""

    @staticmethod
    def dump(table: Table, filepath: str) -> None:
        """Dumps a table into a JSON file."""
        root: List[Dict] = []
        if table:
            header = table[0]
            for row in table[1:]:
                root.append({header[i].value: row[i].value for i in range(len(header))})
        with open(filepath, "w", encoding="utf-8") as json_file:
            dump(root, json_file, indent=2)

    @staticmethod
    def load(
        table: Table, filepath: str, addr: Optional[str] = None
    ):  # pylint: disable=too-many-branches
        """Loads rows from JSON file to table."""

        def load_root(root: Union[Dict, List]) -> None:
            if isinstance(root, list):  # array root
                if all(isinstance(child, list) for child in root):  # array of arrays
                    for row in root:
                        table.add_row(row)
                elif all(isinstance(child, dict) for child in root):  # array of objects
                    keys: List[Any] = []
                    for obj in root:
                        keys += [k for k in obj if k not in keys]
                    table.add_row(keys)
                    for obj in root:
                        table.add_row((obj.get(key, "") for key in keys))
                else:
                    raise ValueError(
                        "JSON array root contents must be of same type: array or object."
                    )
            elif isinstance(root, dict):
                if addr:
                    if root := root.get(addr, []):
                        load_root(root)
                    else:
                        raise KeyError(
                            f"No key {addr!r} found in the root of JSON file {filepath!r}."
                        )
                else:
                    if all(isinstance(value, list) for value in root.values()):
                        for key, values in root.items():
                            values.insert(0, key)
                            table.add_column(values)
                    elif all(isinstance(value, dict) for value in root.values()):
                        load_root(list(root.values()))
                        table.insert_column(0, ("", *root.keys()))
                    else:
                        raise ValueError("JSON object root structure not supported.")
            else:
                raise ValueError(f"Invalid JSON in {filepath}. Root must be an array or an object.")

        with open(filepath, "r", encoding="utf-8") as json_file:
            root = load(json_file)
        load_root(root)
