# Tabling
Tabling is a Python library for creating highly customizable tables in the console.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [FAQ](#faq)
- [Templates](#templates)
- [UI Design](#ui-design)
- [Conclusion](#conclusion)

## Introduction
Tabling was **inspired by HTML and CSS**. It is **row-centric**, like in HTML tables, but supports **direct column operations**. It can be used not only for tabular data, but also for designing **structured console-based user interfaces** (similar to how HTML tables were once used before the rise of CSS Grid and Flexbox).

The potential use cases are virtually limitless: it all depends on your creativity. Tabling doesn't restrict creativity: it empowers it.

Following the **KISS principle**, Tabling is designed to be simple and efficient, yet flexible enough to achieve complex styling and layouts.

## Features
- **Add/remove** components: rows, columns, cells
- **Sort** rows/columns based on column/row key
- **Find/replace** values with new ones
- **Import/export** table to **json**, **csv**, and more
- **Customize element properties:** background, border, font, margin, padding
- **Customize text properties:** alignment, justification, wrap, direction, visibility
- **CSS-like syntax** e.g., ```border.style``` for CSS ```border-style```
- **Unlimited colors:** [140+ color names](https://htmlcolorcodes.com/color-names/), *all RGB values*, all HEX codes
- **5 border styles:** single, double, dashed, dotted, solid
- **6 font styles:** bold, italic, strikethrough, underline, overline, double-underline

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
```
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
  | `clear()`                                               | Removes all table elements           |
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
Elements are customized through their properties. In order to be customized, an element must first be selected or referenced. The table below shows how to select elements:

  | Element | Method                                  |
  |---------|-----------------------------------------|
  | table   | `table`                                 |
  | row     | `table[row_index]`                      |
  | cell    | `table[row_index][column_index]`        |
  | rows    | `for row in table:`                     |
  | cells   | `for row in table:` `for cell in row:`  |
  | column  | `for row in table:` `row[column_index]` |

Each element has 5 main properties: 
  - **background:** Background of an element
  - **border:** Border around an element
  - **font:** Appearance of text in an element
  - **margin:** Outer spacing of an element
  - **padding:** Inner spacing of an element

Cells have 3 additional properties:
  - **text:** Appearance of cell values/entries
  - **width:** Characters allowed, horizontally
  - **height:** Lines characters allowed, vertically

The table below shows customizable property attributes for elements:

  | Property Attribute    | Description               | Example values                                |
  |-----------------------|---------------------------|-----------------------------------------------|
  | `background.color`    | Background color          | `"red"`, `"255,0,0"`, `"#ff0000"`, `"#f00"`   |
  | `border.style`        | Border style              | `"single"`, `"double"`, `"dashed"`, `"solid"` |
  | `border.color`        | Border color              | `"red"`, `"255,0,0"`, `"#ff0000"`, `"#f00"`   |
  | `border.left.style`   | Border-left style         | `"single"`, `"double"`, `"dashed"`, `"solid"` |
  | `border.left.color`   | Border-left color         | `"red"`, `"255,0,0"`, `"#ff0000"`, `"#f00"`   |
  | `border.right.style`  | Border-left style         | `"single"`, `"double"`, `"dashed"`, `"solid"` |
  | `border.right.color`  | Border-right color        | `"red"`, `"255,0,0"`, `"#ff0000"`, `"#f00"`   |
  | `border.top.style`    | Border-top style          | `"single"`, `"double"`, `"dashed"`, `"solid"` |
  | `border.top.color `   | Border-top color          | `"red"`, `"255,0,0"`, `"#ff0000"`, `"#f00"`   |
  | `border.bottom.style` | Border-bottom style       | `"single"`, `"double"`, `"dashed"`, `"solid"` |
  | `border.bottom.color` | Border-bottom color       | `"red"`, `"255,0,0"`, `"#ff0000"`, `"#f00"`   |
  | `font.style`          | Font style                | `"bold"`, `"italic"`, `"strikethrough"`       |
  | `font.color`          | Font color                | `"red"`, `"255,0,0"`, `"#ff0000"`, `"#f00"`   |
  | `margin.left`         | Margin to the left        | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, ...   |
  | `margin.right`        | Margin to the right       | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, ...   |
  | `margin.top`          | Margin to the top         | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, ...   |
  | `margin.bottom`       | Margin to the bottom      | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, ...   |
  | `padding.left`        | Padding to the left       | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, ...   |
  | `padding.right`       | Padding to the right      | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, ...   |
  | `padding.top`         | Padding to the top        | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, ...   |
  | `padding.bottom`      | Padding to the bottom     | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, ...   |
  | `text.justify`        | Direction to justify text | `"left"`, `"center"`, `"right"`               |
  | `text.align`          | Edge to valign text       | `"top"`, `"center"`, `"bottom" `              |
  | `text.wrap`           | Whether to wrap text      | `True`, `False`                               |
  | `text.visible`        | Whether to show text      | `True`, `False`                               |
  | `text.reverse`        | Whether to reverse text   | `True`, `False`                               |
  | `text.letter_spacing` | Spacing between letters   | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, ...   |
  | `text.word_spacing`   | Spacing between words     | `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, ...   |

#### Example
```python
table.border.style = "single"
table[0].font.style = "bold"
table[0].border.bottom.style = "single"
for row in table:
    row[1].text.justify = "center"
    row[2].text.justify = "center"
```
**Note:** To save time and effort, you can copy & paste **code for commonly used table styles** from the **[templates](#templates)** section.

### 5. Display
```python
print(table)
```

![table](https://github.com/user-attachments/assets/94b83266-1690-479e-92f2-de342539caaf)

## FAQ

1. **What is the format for RGB colors?**\
`rrr,ggg,bbb`

2. **What is the format for HEX colors?**\
`#rrggbb` or `#rgb`

3. **How do I set a column width?**\
Set the `cell.width` of any cell within the column to the desired column width.

4. **How do I set a row height?**\
Set the `cell.height` of any cell within the row to the desired row height.

5. **Why are colors not displaying as expected?**\
Use your OS's native terminal instead of an IDE terminal.


6. **How to make `table.sort_rows` exclude the first row?**\
Use argument `start=1`.

7. **How to make `table.sort_rows` exclude the last row?**\
Use argument `stop=-1`

8. **How to fix row lines leaking to next line for small terminal window?**\
Resize, and/or zoom out, the terminal window to fit the rows.

9. **Why do borders overlap when I use emojis?**\
Emojis, such as smileys, consists of two parts: structure and color. Python takes these emojis as having a length of 1, but most terminals take them as having a length of 2. Thus, terminals use two spaces to render the emoji while Python had reserved only one. Thus the overlaps.

## Templates
These are pre-written code blocks used to quickly, and effectively, customize a table with a **commonly used table styles**.

1. **plain**  
    ![template-plain](https://github.com/user-attachments/assets/4b584de6-e097-4511-a9b2-fe629334f8cd)

    ```python
    # No customization
    ```

2. **simple**  
    ![template-simple](https://github.com/user-attachments/assets/dfad33e7-48a8-4ee7-a984-c6ebba8c3935)

    ```python
    table.border.style = "single"
    ```

3. **headed**  
    ![template-headed](https://github.com/user-attachments/assets/73cca6e9-e681-46e4-896b-3352752b5b7b)

    ```python
    # Configuration
    BORDER_STYLE = "single"
    
    # Customization
    table.border.style = BORDER_STYLE
    table[0].border.bottom.style = BORDER_STYLE
    ```

4. headed & footed  
    ![template-headed-footed](https://github.com/user-attachments/assets/0a4afa53-854a-4b63-a581-bd58494477df)

    ```python
    # Configuration
    BORDER_STYLE = "single"
    
    # Customization
    table.border.style = BORDER_STYLE
    table[0].border.bottom.style = BORDER_STYLE
    table[-1].border.top.style = BORDER_STYLE
    ```

5. grid  
    ![template-grid](https://github.com/user-attachments/assets/aadb93b7-bda4-4e76-8eb6-d7596f7aa433)

    ```python
    # Configuration
    BORDER_STYLE = "single"
    COLUMN_SPACING = 0
    
    # Customization
    table.colspacing = COLUMN_SPACING
    for row in table:
        for cell in row:
            cell.border.style = BORDER_STYLE
    ```

6. collapsed grid  
    ![template-collapsed-grid](https://github.com/user-attachments/assets/a0273a3e-1164-46f0-bd23-5a32aa8d69b2)

    ```python
    # Configuration
    BORDER_STYLE = "single"
    COLUMN_SPACING = 0
    
    # Customization
    table.colspacing = COLUMN_SPACING
    for row in table:
        for cell in row:
            cell.border.left.style = BORDER_STYLE
            cell.border.top.style = BORDER_STYLE
        row[-1].border.right.style = BORDER_STYLE
    for cell in table[-1]:
        cell.border.bottom.style = BORDER_STYLE
    ```

7. staked  
    ![template-stacked](https://github.com/user-attachments/assets/51c23e1b-ce66-4cd7-95fe-98071f641853)

    ```python
    for row in table:
        row.border.style = "single"
    ```

8. stacked-collapsed  
    ![template-striped](https://github.com/user-attachments/assets/c8ca3399-47a8-4543-b8d6-13a593068657)

    ```python
    # Configuration
    BORDER_STYLE = "single"
    ROW_SPACING = 1
    
    # Customization
    table.rowspacing = 0  # !important
    for row in table:
        row.border.style = BORDER_STYLE
        row.border.top.style = None
        row.padding.block = ROW_SPACING // 2, ROW_SPACING - (ROW_SPACING // 2)
    table[0].border.top.style = BORDER_STYLE
    ```

9. queued  
    ![template-queued](https://github.com/user-attachments/assets/804406ba-63a5-4c04-a05e-aec47d320415)

    ```python
    # Configuration
    BORDER_STYLE = "single"
    ROW_SPACING = 0
    COLUMN_SPACING = 0
    
    # Customization
    table.rowspacing = 0  # !important
    table.colspacing = COLUMN_SPACING
    for cell in table[0]:
        cell.border.top.style = BORDER_STYLE
    for row in table:
        for cell in row:
            cell.border.left.style = BORDER_STYLE
            cell.border.right.style = BORDER_STYLE
        row[0].padding.block = ROW_SPACING // 2, ROW_SPACING - (ROW_SPACING // 2)
    for cell in table[-1]:
        cell.border.bottom.style = BORDER_STYLE
    ```

  10. queued-collapsed  
    ![queued-collapsed](https://github.com/user-attachments/assets/9bd756d4-3645-4995-964f-50912d5a9473)

    ```python
    # Configuration
    BORDER_STYLE = "single"
    ROW_SPACING = 0
    COLUMN_SPACING = 0
    
    # Customization
    table.rowspacing = 0  # !important
    table.colspacing = COLUMN_SPACING
    for cell in table[0]:
        cell.border.top.style = BORDER_STYLE
    for row in table:
        for cell in row:
            cell.border.left.style = BORDER_STYLE
            cell.border.right.style = BORDER_STYLE
        row[0].padding.block = ROW_SPACING // 2, ROW_SPACING - (ROW_SPACING // 2)
    for cell in table[-1]:
        cell.border.bottom.style = BORDER_STYLE
    ```

11. checkered  
![template-checkered](https://github.com/user-attachments/assets/dfa0fc80-3059-4c04-ba35-cf9a0a4e27c8)

    ```python
    # Configuration
    BORDER_STYLE = None
    PADDING_INLINE = 1
    PADDING_BLOCK = 1
    ALT_BG_COLOR = "#999"
    
    # Customization
    table.rowspacing = 0  # !important
    table.colspacing = 0  # !important
    for row in table:
        for cell in row:
            cell.border.style = BORDER_STYLE
            cell.padding.inline = PADDING_INLINE, PADDING_INLINE
            cell.padding.block = PADDING_BLOCK, PADDING_BLOCK
        for row in table[0::2]:
            for cell in row[0::2]:
                cell.background.color = ALT_BG_COLOR
        for row in table[1::2]:
            for cell in row[1::2]:
                cell.background.color = ALT_BG_COLOR
    ```

## UI Design

Like HTML, **Tabling** enables you to create structured, grid-based user interfaces (UIs) using tables. The kinds of interfaces you can design **depend entirely on your creativity** and your ability to break complex layouts into table-like components. In short, ***the sky’s the limit!***

This section showcases real-world examples and source code demonstrating how Tabling can be used to build console-based UIs and structured layouts.

1. chess board  
    ![interface-chess-board](https://github.com/user-attachments/assets/b2863c8f-4e97-4838-9e1b-aa65348dff79)

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

2. calculator  
    ![interface-calculator](https://github.com/user-attachments/assets/a3a791ea-da08-48a1-b22b-605e46b078f9)

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

3. phone  
    ![interface-phone](https://github.com/user-attachments/assets/1551b2c7-c75c-474f-823d-9df34ff8e801)

    ```python
    from tabling import Table

    SCREEN_HEIGHT = 12

    phone = Table(colspacing=1, rowspacing=0)
    phone.border.style = "single"
    for _ in range(SCREEN_HEIGHT):
        phone.add_row(("","",""))
    phone.add_row(("...", "", "..."))
    phone.add_row(("", "▢", ""))
    phone.add_row(("╭─╮", "", "╭─╮"))
    phone.add_row(("1∞", "2abc", "3def"))
    phone.add_row(("4ghi", "5jkl", "6mno"))
    phone.add_row(("7pqrs", "8tuv", "9wxyz"))
    phone.add_row(("*^+", "0 ␣", "#⍽⇧"))

    phone.padding.inline = 1, 1
    # Screen
    phone[0].border.top.style = "single"
    for row in phone[:SCREEN_HEIGHT]:
        row.border.left.style = "single"
        row.border.right.style = "single"
    phone[SCREEN_HEIGHT-1].border.bottom.style = "single"

    # Buttons
    home_btn = phone[SCREEN_HEIGHT + 1][1]
    home_btn.border.style = "single"
    home_btn.text.justify = "center"
    home_btn.width = 5

    for row in phone[SCREEN_HEIGHT + 3:]:
        row.margin.top = 1

    print(phone)
    ```

4. barcode  
    ![interface-barcode](https://github.com/user-attachments/assets/97d9ce75-4797-4384-babb-993086c75b51)

    ```python
    from tabling import Table

    barcode = Table(colspacing=1, rowspacing=0)
    barcode.add_row("")
    barcode.add_row((6, "", 0, 0, 1, 0, 8, 7, ""))
    barcode[0][0].height = 10
    barcode[0][1].border.right.style = "double"
    barcode[1][1].border.right.style = "double"
    barcode[0][2].border.left.style = "solid"
    barcode[0][3].border.left.style = "single"
    barcode[0][4].border.left.style = "solid"
    barcode[0][5].border.left.style = "single"
    barcode[0][6].border.left.style = "solid"
    barcode[0][7].border.left.style = "solid"
    barcode[0][8].border.left.style = "double"
    barcode[1][8].border.left.style = "double"
    
    print(barcode)
    ```

5. menu  
    ![interface-menu](https://github.com/user-attachments/assets/569ab58c-8b4c-4171-bd6e-98f13340e134)

    ```python    
    from tabling import Table

    question = "What's your favorite programming language?"
    choices = ("Python", "C", "C++", "Javascript")
    options = (f"{i}." for i in range(1, len(choices) + 1))

    menu = Table(colspacing=1, rowspacing=0)
    menu.add_column(options)
    menu.add_column(choices)
    menu.padding.left = 2

    print(question)
    print(menu)

    option = int(input("> "))
    print(f"You chose: {menu[option-1][1]}")
    ```

6. calendar  
    ![interface-calendar](https://github.com/user-attachments/assets/5a2aff4e-5c04-479d-883f-5d18d42fd94f)

    ```python
    from tabling import Table

    calendar = Table(colspacing=0, rowspacing=0)
    
    calendar.add_row(("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"))
    calendar.add_row(("", "", "", "", 1, 2, 3))
    calendar.add_row((4, 5, 6, 7, 8, 9, 10))
    calendar.add_row((11, 12, 13, 14, 15, 16, 17))
    calendar.add_row((18, 19, 20, 21, 22, 23, 24))
    calendar.add_row((25, 26, 27, 28, 29, 30, 31))
    
    calendar[0].font.style = "bold"
    for row in calendar:
        for cell in row:
            cell.width = 3
            cell.height = 2
            cell.border.left.style = "single"
            cell.border.top.style = "single"
        row[-1].border.right.style = "single"
    for cell in calendar[-1]:
        cell.border.bottom.style = "single"
    for cell in calendar[0]:
        cell.height = 1
        cell.text.justify = "center"
    
    print(" May 2025")
    print(calendar)
    ```


7. form  
    ![interface-form](https://github.com/user-attachments/assets/60fd6cbc-20b5-4960-9c4f-71dd93a08d6d)

    ```python
    from tabling import Table

    form = Table(colspacing=2, rowspacing=0)
    form.add_row(("First Name", "Enter your first name"))
    form.add_row(("Last Name", "Enter your last name"))
    form.add_row(("Gender", "○ Male ○ Female"))
    form.add_row(("Email", "Enter your email"))
    form.add_row(("Phone Number", "Enter your phone number"))
    form.add_row(("Username", "Enter your username"))
    form.add_row(("Password", "Enter your password"))
    form.add_row(("Confirm Password", "Confirm your password"))
    
    form.border.style = "single"
    form.padding.inline = 1, 1
    for row in form:
        row[1].width = 25
        row[1].font.color = "#999"
        row[1].font.style = "italic"
        row[1].border.style = "single"
        row[1].padding.inline = 1, 1
    form[2][1].border.style = None
    form[2][1].padding.block = 1, 1
    
    form.add_row(("", "Register"))
    # form[-1][1].text.justify = "right"
    form[-1].border.style = "single"
    form[-1].background.color = "lightgray"
    form[-1].margin.top = 1
    form[-1].font.style = "bold"
    form[-1].padding.block = 1, 1
    
    print(form)
    ```

8. navigation bar  
    ![interface-navigation-bar](https://github.com/user-attachments/assets/7a88be1f-7397-4dbb-9c1d-e57f0213cf52)

    ```python
    from tabling import Table

    navbar = Table(colspacing=0, rowspacing=0)

    navbar.add_row(("⌂", "Home"))
    navbar.add_row(("⟟", "Search"))
    navbar.add_row(("✩", "Favorites"))
    navbar.add_row(("☺", "Account"))
    navbar.add_row(("⚙", "Settings"))
    navbar.add_column(("", "", "Some account stuff", "", ""))

    navbar.border.style = "single"
    navbar.padding.inline = 1, 1
    for cell in navbar[0][2:]:
        cell.border.top.style = "single"
    for cell in navbar[-1][2:]:
        cell.border.bottom.style = "single"
    for row in navbar:
        for cell in row:
            cell.padding.left = 1
        row[2].border.left.style = "single"
        row[2].border.right.style = "single"
        row[2].width = 25
        row[2].padding.block = 1, 1
        row[2].text.justify = "center"
    navbar[3][0].background.color = "gray"
    navbar[3][1].background.color = "gray"
    navbar[3][1].font.style = "bold"

    print(navbar)
    ```
9. bar graph  
    ![interface-bar-graph](https://github.com/user-attachments/assets/4b172d55-de97-4169-8064-647fb778c0aa)

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

10. flag  
    ![interface-flag](https://github.com/user-attachments/assets/7da56463-c676-43d4-b2ff-c6fbc1de9514)

    ```python
    from tabling import Table

    flag = Table(colspacing=0, rowspacing=0)
    for _ in range(3):
        flag.add_column(" ")
    for cell in flag[0]:
        cell.height = 10
        cell.width = 10
    flag[0][0].background.color = "blue"
    flag[0][1].background.color = "white"
    flag[0][2].background.color = "red"

    print(flag)
    ```

## Conclusion

**Tabling** transforms the way you think about console output. What begins as simple table rendering evolves into a powerful system for building structured, styled, and responsive interfaces—right in the terminal.

Whether you're formatting data, sketching UI prototypes, or building full-fledged console applications, Tabling gives you the building blocks to do it with precision and style. You get the control of CSS, the structure of HTML, and the flexibility of Python—all in one elegant toolkit.

This isn't just about tables. It's about rethinking what's possible in plain text environments.

So go ahead—build tables, draw dashboards, design forms, simulate components.
Create what you imagine. Directly in your terminal.

**Remember:**
*“Tabling is a powerful tool not because of what it does, but because of what it enables you to do.”* — Haripo Wesley T.
