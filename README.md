# Tabling
[![PyPI - Version](https://img.shields.io/pypi/v/tabling)](https://pypi.org/project/tabling/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/tabling)](https://pypi.org/project/tabling/)
[![License](https://img.shields.io/pypi/l/tabling)](https://github.com/haripowesleyt/tabling/blob/main/LICENSE)
[![Python Versions](https://img.shields.io/pypi/pyversions/tabling)](https://pypi.org/project/tabling/)

Tabling is a Python library for creating highly customizable tables in the console.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Templates](#templates)
- [Effects](#effects)
- [Applications](#applications)
- [Contributing](#contributing)
- [License](#license)
- [Conclusion](#conclusion)

## Introduction
Tabling was **inspired by HTML and CSS**. It is **row-centric**, like in HTML tables, but supports **direct column operations**. It can be used not only for tabular data but also for designing **user interfaces in the console** (similar to how HTML tables were once used before the rise of CSS Grid and Flexbox).

## Features
- **Add/remove** rows, columns, cells
- **Sort** rows/columns based on key
- **Find/replace** values with new ones
- **Import/export** table to **JSON**, **CSV**, **TXT**
- **Customize** `background`, `border`, `font`, `margin`, `padding`
- **Modify text** alignment, justification, wrap, direction, visibility
- **CSS-like syntax** e.g., `border.style` for CSS `border-style`
- **[140+ color names](https://htmlcolorcodes.com/color-names/)**; **all RGB values**; & **all HEX color codes**
- **5 border styles:** `single`, `double`, `dashed`, `dotted`, `solid`
- **5+ font styles:** `bold`, `italic`, `strikethrough`, `underline`

## Installation
```bash
pip install tabling
```

## Usage

### 1. Import library
```python
from tabling import Table
```

### 2. Create table
```python
table = Table(colspacing=1, rowspacing=0)
```

### 3. Perform operations
The table below shows available Tabling table operations:
  | Method                                                  |  Description                         |
  |---------------------------------------------------------|--------------------------------------|
  | `add_row(entries: Iterable)`                            | Adds a row                           |
  | `add_column(entries: Iterable)`                         | Adds a column                        |
  | `insert_row(index: int, entries: Iterable)`             | Inserts a row at an index            |
  | `insert_column(index: int, entries: Iterable)`          | Inserts a column at an index         |
  | `remove_row(index: int)`                                | Removes the row at an index          |
  | `remove_column(index: int)`                             | Removes the column at an index       |
  | `swap_rows(index1: int, index2: int)`                   | Swaps positions of two rows          |
  | `swap_columns(index1: int, index2: int)`                | Swaps positions of two columns       |
  | `sort_rows(key: int, start=0, reverse=False)`           | Sorts rows by a key column           |
  | `sort_columns(key: int, start=0, reverse=False)`        | Sorts columns by a key row           |
  | `find(value: Any)`                                      | Prints a table, highlighting matches |
  | `replace(value: Any, repl: Any)`                        | Replaces a value with a new one      |
  | `export_csv(filepath: str)`                             | Exports rows to csv file             |
  | `import_csv(filepath: str)`                             | Imports rows from csv file           |
  | `export_json(filepath: str, key=None, as_objects=True)` | Exports rows to json file            |
  | `import_json(filepath: str, key=None)`                  | Imports rows from json file          |
  | `export_txt(filepath: str)`                             | Exports plain table to txt file      |

#### Example
```python
table.add_row(("Name", "Age", "Sex"))
table.add_row(("Wesley", 20, "M"))
table.add_row(("Ashley", 12, "F"))
table.add_row(("Lesley", 12, "M"))
table.add_column(("Married", True, False, False))
```

### 4. Customize
The table below describes all customizable element properties:

  | Property Attribute    | Description               | Example values                   |
  |-----------------------|---------------------------|----------------------------------|
  | `background.color`    | Background color          | red, green, blue, black, white   |
  | `border.style`        | Border style              | single, double, dashed, solid    |
  | `border.color`        | Border color              | red, green, blue, black, white   |
  | `border.left.style`   | Border-left style         | single, double, dashed, solid    |
  | `border.left.color`   | Border-left color         | red, green, blue, black, white   |
  | `border.right.style`  | Border-right style        | single, double, dashed, solid    |
  | `border.right.color`  | Border-right color        | red, green, blue, black, white   |
  | `border.top.style`    | Border-top style          | single, double, dashed, solid    |
  | `border.top.color `   | Border-top color          | red, green, blue, black, white   |
  | `border.bottom.style` | Border-bottom style       | single, double, dashed, solid    |
  | `border.bottom.color` | Border-bottom color       | red, green, blue, black, white   |
  | `font.style`          | Font style                | bold, italic, strikethrough      |
  | `font.color`          | Font color                | red, green, blue, black, white   |
  | `margin.left`         | Margin to the left        | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
  | `margin.right`        | Margin to the right       | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
  | `margin.top`          | Margin to the top         | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
  | `margin.bottom`       | Margin to the bottom      | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
  | `padding.left`        | Padding to the left       | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
  | `padding.right`       | Padding to the right      | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
  | `padding.top`         | Padding to the top        | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
  | `padding.bottom`      | Padding to the bottom     | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
  | `text.justify`        | Horizontal text alignment | left, center, right              |
  | `text.align`          | Vertical text alignment   | top, center, bottom              |
  | `text.wrap`           | Whether to wrap text      | True, False                      |
  | `text.visible`        | Whether to show text      | True, False                      |
  | `text.reverse`        | Whether to reverse text   | True, False                      |
  | `text.letter_spacing` | Spacing between letters   | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
  | `text.word_spacing`   | Spacing between words     | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |


The table below shows how to reference elements for customization:

  | Element | Method                           |
  |---------|----------------------------------|
  | table   | `table`                          |
  | row     | `table[row_index]`               |
  | cell    | `table[row_index][column_index]` |
  | rows    | `for row in table:`              |
  | cells   | `for cell in row:`               |

#### Example
```python
table.border.style = "single"
table[0].font.style = "bold"
for row in table:
    row[1].text.justify = "center"
    row[2].text.justify = "center"
```

### 5. Display
```python
print(table)
```

![table](https://raw.githubusercontent.com/haripowesleyt/tabling/main/assets/images/print-table.png)

## Templates
Templates are pre-written, border-related, styles you can copy and customize.

### 1. Headed
Adds a border between the header and body.

```
table.border.style = "single"
table[0].border.bottom.style = "single"
table[1].margin.top = max(0, table.rowspacing - 1)
for row in table[2:]:
    row.margin.top = max(0, table.rowspacing)
table.rowspacing = 0
```

![template-headed](https://raw.githubusercontent.com/haripowesleyt/tabling/main/assets/images/template-headed.png)

### 2. Stacked
Creates a stack of rows with collapsed horizontal borders.

```python
table.border.style = "single"
for row in table[1:]:
    row.border.top.style = "single"
```

![template-stacked](https://raw.githubusercontent.com/haripowesleyt/tabling/main/assets/images/template-stacked.png)

### 3. Queued
Creates column-separated borders with equal column spacing.

```python
for cell in table[0]:
    cell.border.top.style = "single"
for row in table:
    for cell in row:
        cell.border.left.style = "single"
        cell.border.right.style = "single"
    row[0].height += table.rowspacing
for cell in table[-1]:
    cell.border.bottom.style = "single"
for cell in table[0]:
    cell.width += table.colspacing
table.rowspacing = table.colspacing = 0
```

![template-queued](https://raw.githubusercontent.com/haripowesleyt/tabling/main/assets/images/template-queued.png)

### 4. Queued - Collapsed
Collapses horizontal borders while keeping column structure.

```python
for cell in table[0]:
    cell.border.top.style = "single"
for row in table:
    for cell in row:
        cell.border.left.style = "single"
    row[-1].border.right.style = "single"
    row[0].height += table.rowspacing
for cell in table[-1]:
    cell.border.bottom.style = "single"
for cell in table[0]:
    cell.width += table.colspacing
table.rowspacing = table.colspacing = 0
```

![queued-collapsed](https://raw.githubusercontent.com/haripowesleyt/tabling/main/assets/images/template-queued-collapsed.png)

### 5. Grid
Adds full borders to every cell.

```python
for row in table:
    for cell in row:
        cell.border.style = "single"
```

![template-grid](https://raw.githubusercontent.com/haripowesleyt/tabling/main/assets/images/template-grid.png)

### 6. Grid - Collapsed
A compact version of the grid layout with collapsed cell borders.

```python
table.border.style = "single"
for row in table:
    for cell in row[:-1]:
        cell.border.right.style = "single"
    row[0].height += table.rowspacing
for row in table[:-1]:
    for cell in row:
        cell.border.bottom.style = "single"
for cell in table[0]:
    cell.width += table.colspacing
table.rowspacing = table.colspacing = 0
```

![template-collapsed-grid](https://raw.githubusercontent.com/haripowesleyt/tabling/main/assets/images/template-grid-collapsed.png)

## Effects
Effects are pre-written, color-related, styles you can copy and customize.

### 1. Striped
Alternates row colors.

```python
for row in table[1::2]:
    row.background.color = "#999"
```

![effect-striped](https://raw.githubusercontent.com/haripowesleyt/tabling/main/assets/images/effect-striped.png)

### 2. Banded
Alternates column colors.

```python
for row in table:
    for cell in row[1::2]:
        cell.background.color = "#999"
```

![effect-banded](https://raw.githubusercontent.com/haripowesleyt/tabling/main/assets/images/effect-banded.png)

### 3. Checkered
Alternates every cell’s color for a chessboard-like effect.

```python
table.background.color = "#333"
for row in table:
    row[0].height += table.rowspacing
for row in table[0::2]:
    for cell in row[0::2]:
        cell.background.color = "#222"
for row in table[1::2]:
    for cell in row[1::2]:
        cell.background.color = "#222"
for cell in table[0]:
    cell.width += table.colspacing
table.rowspacing = table.colspacing = 0
```

![effect-checkered](https://raw.githubusercontent.com/haripowesleyt/tabling/main/assets/images/effect-checkered.png)

## Applications
These are real world examples where Tabling was used to design **console-based user interfaces**.

### 1. Menu
A menu-driven interface where a user selects a numbered option.

```python    
from tabling import Table

question = "What's your favorite programming language?"
answers = ("Python", "C", "C++", "Javascript")
options = (f"{i}." for i in range(1, len(answers) + 1))

menu = Table(colspacing=1, rowspacing=0)
menu.add_column(options)
menu.add_column(answers)
menu.padding.left = 2

print(question)
print(menu)

option = int(input("> "))
print(f"You chose: {menu[option-1][1]}")
```

![application-menu](https://raw.githubusercontent.com/haripowesleyt/tabling/main/assets/images/application-menu.png)

### 2. Calendar
A customizable calendar for May 2025.

```python
from tabling import Table

calendar = Table(colspacing=0, rowspacing=0)

calendar.add_row(("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"))
calendar.add_row(("", "", "", "", 1, 2, 3))
calendar.add_row((4, 5, 6, 7, 8, 9, 10))
calendar.add_row((11, 12, 13, 14, 15, 16, 17))
calendar.add_row((18, 19, 20, 21, 22, 23, 24))
calendar.add_row((25, 26, 27, 28, 29, 30, 31))

calendar[0].background.color = "#888"
calendar[3][3].background.color = "lightgray"
for row in calendar:
    row[0].background.color = "#999"
    for cell in row:
        cell.width = 5
        cell.height = 2
        
print(" May 2025")
print(calendar)
```

![interface-calendar](https://raw.githubusercontent.com/haripowesleyt/tabling/main/assets/images/application-calendar.png)

### 3. Bar Graph
A terminal-based bar graph made using Tabling.

```python
from tabling import Table

graph = Table(colspacing=4)
graph.add_column((12, 10, 8, 6, 4, 2))
for _ in range(4):
    graph.add_column(("", "", "", "", "", ""))

for column_index in range(1, 5):
    graph[0][column_index].width = 6

graph.margin.top = 1
graph[0][-1].margin.right = 3
graph[-1].border.bottom.style = "single"
for row_index, row in enumerate(graph):
    row[0].border.right.style = "single"
    row[0].height = 3
    if row_index > 2:
        row[1].background.color = "tomato"
    if row_index > 3:
        row[2].background.color = "crimson"
    if row_index > 0:
        row[3].background.color = "maroon"
    if row_index > 1:
        row[4].background.color = "brown"

graph.add_row(("", "A","B", "C", "D"))
for cell in graph[-1]:
    cell.text.justify = "center"

print(graph)
```

![interface-bar-graph](https://raw.githubusercontent.com/haripowesleyt/tabling/main/assets/images/application-bar-graph.png)

### 4. Calculator
A terminal-based calculator interface using Tabling.

```python
from tabling import Table

SCREEN_HEIGHT = 10

calculator = Table(colspacing=1, rowspacing=0)
calculator.border.style = "solid"
for _ in range(SCREEN_HEIGHT):
    calculator.add_row(("", "", "", "", ""))
calculator.add_row(("Menu", "⯇", "⏵", "⨯", "AC"))
calculator.add_row(("DEG", "sin", "cos", "tan", "π"))
calculator.add_row(("Shift", "√x", "ⁿ√x", "(", ")"))
calculator.add_row(("%", "x²", "xⁿ", "□∕□", "÷"))
calculator.add_row(("log", 7, 8, 9, "×"))
calculator.add_row(("ln", 4, 5, 6, "−"))
calculator.add_row(("e", 1, 2, 3, "+"))
calculator.add_row(("□", "Ans", 0, ".", "="))

calculator[0].border.top.style = "single"
for row in calculator[:SCREEN_HEIGHT]:
    row.border.left.style = "single"
    row.border.right.style = "single"
calculator[SCREEN_HEIGHT - 1].border.bottom.style = "single"

for row in calculator[SCREEN_HEIGHT:]:
    for cell in row: 
        cell.width = 5
        cell.text.justify = "center"
        cell.border.style = "single"

print(calculator)
```

![interface-calculator](https://raw.githubusercontent.com/haripowesleyt/tabling/main/assets/images/application-calculator.png)

### 5. Chess Board
A fully drawn chess board using Tabling.

```python
from tabling import Table

chess_board = Table(colspacing=0, rowspacing=0)

for _ in range(8):
    chess_board.add_row(("",)*8)

chess_board.font.style = "bold"
chess_board.background.color = "burlywood"
for row in chess_board:
    for cell in row:
        cell.padding.block = 1, 1
        cell.padding.inline = 2, 2
for row in chess_board[0::2]:
    for cell in row[0::2]:
        cell.background.color = "#333"
for row in chess_board[1::2]:
    for cell in row[1::2]:
        cell.background.color = "#333"
chess_board.insert_column(0, range(8, 0, -1))
chess_board.add_column(range(8, 0, -1))
chess_board.add_row(" ABCDEFGH")
chess_board.insert_row(0, " ABCDEFGH")

print(chess_board)
```

![interface-chess-board](https://raw.githubusercontent.com/haripowesleyt/tabling/main/assets/images/application-chess-board.png)

## FAQ/Troubleshooting

1. How do I enter RGB and HEX colors?  
Use r,g,b for RGB (e.g., 255,0,0) and #rrggbb or #rgb for HEX (e.g., #ff0000 or #f00)

2. How do I change a cell value?  
Use `table[row_index][column_index].value = new_value`

3. How do I check the data type of a cell value?  
Use `type(cell.value)`. Cell values are stored as provided by the user.

4. How can I implement cell merging?  
Currently, Tabling does not support cell merging (rowspan, colspan). However, you can simulate merged cells by adjusting width, height, padding, and border properties across adjacent cells to create the visual illusion of merging.

5. Is there a shorter way to set margin and padding of all sides?  
Taking margin and padding as just spacing, use `spacing.inline = left, right` to set spacing-left and spacing-right and `spacing.block = top, bottom` to set spacing-top and spacing-bottom. For example, `margin.top = 2, 1` sets `margin.top = 2` and `margin.bottom = 1`.

6. Can table rendering be made a bit faster?  
Yes, by setting `table.preserve = False`. This means that normalization changes will directly affect the original table. In contrast, setting `table.preserve = True` creates a copy of the table each time it needs to be rendered. Preservation is safe and predictable but slower, whereas disabling preservation is faster but can be unsafe and unpredictable.

7. Why are rows, longer than my terminal, leaking to new lines?  
Most terminals wrap text when it's longer than their current width. Resize your terminal or zoom out to fit long rows. If they still don't fit,  use `print(f"\x1b[?7l{table}\x1b[?7h")` to truncate the rows at the terminal width. Alternatively, use `table.export_txt(filepath)` to export the plain table to a text file, and then open the file with a non-wrapping editor.

8. Why are some colors not shown as expected?  
Make sure you use your Operating System's native terminal to display the table. IDE, such as VS Code (old versions), offer a terminal that is not as complete as an OS's terminal. The missing features might be essential for rendering the table. So, either update your IDE to the latest version, or use your OS's terminal (Recommended).

9. What is a `key` when importing/exporting to JSON files?  
A key is like an address where the rows and columns are stored (when importing) or are to be stored (when exporting). A key must only be used where a JSON file has or is to have an object root. For an array root, leave the key as None. Ideally a key must be like a table title, but it can be named anything.

10. Are there any other import/export file types to be supported?  
Yes, many of them. Excel files support (using openpyxl) is currently in beta phase. HTML and PDF files are in the alpha phase. These features will be released once they reach stable.

## Contributing

Contributions are welcome and appreciated! Whether it's a bug report, feature suggestion, or a pull request, your input helps make **Tabling** a better tool for everyone.

Follow the following steps when contributing:
1. Fork the repository  
Click the Fork button at the top right of the [GitHub repository](https://github.com/haripowesleyt/tabling) to create your own copy
2. Clone your fork  
    ```bash
    git clone https://github.com/<your-username>/tabling.git
    cd tabling
    ```
3. Create a new branch
   ```bash
   git checkout -b feature/my-new-feature
   ```
4. Make your changes  
    - Use tools like black, pylint, and mypy for code changes
    - Make sure your changes do not break existing functionality
    - Update documentation if needed
5. Commit your changes
   ```bash
   git commit -m "feat: add my new feature"
   ```
6. Push your fork
   ```bash
   git push origin feature/my-new-feature
   ```

7. Create a Pull Request  
   Go to the original repository and open a pull request with a clear description of your changes. 

## License
This project is licensed under the **MIT License** – see the [LICENSE](https://raw.githubusercontent.com/haripowesleyt/tabling/main/LICENSE) file for details.

## Conclusion

**Tabling** makes it easy to create clean, customizable tables in the terminal. It’s fast, flexible, and built with a CSS-like approach that’s intuitive for anyone familiar with web design. Whether you're formatting data or building full console interfaces, Tabling gets out of your way and lets you focus on structure and style. Simple as that.

> “Tabling is a powerful tool not because of what it does, but because of what it enables you to do.” — Haripo Wesley T.