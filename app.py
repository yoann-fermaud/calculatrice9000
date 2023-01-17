from tkinter import *

DIGITS_FONT_COLOR = "#FFFFFF"

DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DIGITS_RESULT_FONT_STYLE = ("Arial", 32, "bold")

DEFAULT_BG_COLOR = "#000000"
DEFAULT_BG_COLOR_BUTTON = "#252525"

SPECIAL_BG_COLOR = "#FF9500"

expression = ""


def press_button(key):
    if key == "=":
        calculate_expression()
        return
    elif key == "C":
        clear_expression()
        return

    global expression
    expression += str(key)
    equation.set(expression)


def calculate_expression():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total[:4])
        expression = total[:4]
    except:
        equation.set("Error")
        expression = ""


def clear_expression():
    global expression
    expression = ""
    equation.set("")


if __name__ == '__main__':
    window = Tk()
    window.configure(bg=DEFAULT_BG_COLOR)
    window.geometry("365x665")
    window.resizable(False, False)
    window.title("Calculator")

    equation = StringVar()

    result = Label(window, bg=DEFAULT_BG_COLOR, fg=DIGITS_FONT_COLOR, textvariable=equation,
                   font=DIGITS_RESULT_FONT_STYLE, height=3)
    result.grid(row=0, columnspan=4)

    buttons = ["C", "\u221a", "x²", "/", 7, 8, 9, "x", 4, 5, 6, "-", 1, 2, 3, "+", 0, "\t", ",", "="]

    grid_row = 1
    grid_column = 0

    for element in buttons:
        if element == "C":
            button = Label(window, text=str(element), bg=SPECIAL_BG_COLOR, fg=DIGITS_FONT_COLOR,
                           font=DIGITS_FONT_STYLE, height=2, width=4)
            button.grid(row=grid_row, column=grid_column, sticky=NSEW)
            button.bind("<Button-1>", lambda event: press_button("C"))
        elif element == "\u221a":
            button = Label(window, text=str(element), bg=DEFAULT_BG_COLOR_BUTTON, fg=DIGITS_FONT_COLOR,
                           font=DIGITS_FONT_STYLE, height=2, width=4)
            button.grid(row=grid_row, column=grid_column, sticky=NSEW)
            button.bind("<Button-1>", lambda event: press_button("**0.5"))
        elif element == "x²":
            button = Label(window, text=str(element), bg=DEFAULT_BG_COLOR_BUTTON, fg=DIGITS_FONT_COLOR,
                           font=DIGITS_FONT_STYLE, height=2, width=4)
            button.grid(row=grid_row, column=grid_column, sticky=NSEW)
            button.bind("<Button-1>", lambda event: press_button("**2"))
        elif element == "x":
            button = Label(window, text=str(element), bg=DEFAULT_BG_COLOR_BUTTON, fg=DIGITS_FONT_COLOR,
                           font=DIGITS_FONT_STYLE, height=2, width=4)
            button.grid(row=grid_row, column=grid_column, sticky=NSEW)
            button.bind("<Button-1>", lambda event: press_button("*"))
        elif element == "\t":
            button = Label(window, text=str(element), bg=DEFAULT_BG_COLOR_BUTTON, fg=DIGITS_FONT_COLOR,
                           font=DIGITS_FONT_STYLE, height=2, width=4)
            button.grid(row=grid_row, column=grid_column, sticky=NSEW)
        elif element == ",":
            button = Label(window, text=str(element), bg=DEFAULT_BG_COLOR_BUTTON, fg=DIGITS_FONT_COLOR,
                           font=DIGITS_FONT_STYLE, height=2, width=4)
            button.grid(row=grid_row, column=grid_column, sticky=NSEW)
            button.bind("<Button-1>", lambda event: press_button("."))
        else:
            button = Label(window, text=str(element), bg=DEFAULT_BG_COLOR_BUTTON, fg=DIGITS_FONT_COLOR,
                           font=DIGITS_FONT_STYLE, height=2, width=4)
            button.bind("<Button-1>", lambda event, button_e=element: press_button(button_e))
            button.grid(row=grid_row, column=grid_column, sticky=NSEW)

        grid_column += 1
        if grid_column == 4:
            grid_row += 1
            grid_column = 0

    window.mainloop()
