import tkinter as tk
from math import sin, cos, tan, radians, pow, isclose

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error"  # Handle division by zero
    return x / y

def exponentiate(x, y):
    return pow(x, y)

def sine(x):
    return round(sin(radians(x)), 2)  # Converts degrees to radians and calculates sine

def cosine(x):
    return round(cos(radians(x)), 2)  # Converts degrees to radians and calculates cosine

def tangent(x):
    # Handle angles where tan(x) approaches infinity
    if isclose(cos(radians(x)), 0, abs_tol=1e-9):
        return "Infinity"
    else:
        return round(tan(radians(x)), 2)  # Converts degrees to radians and calculates tangent

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""

        # Display widget
        self.display = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="sunken")
        self.display.grid(row=0, column=0, columnspan=5)

        # Buttons
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '(',
            '1', '2', '3', '-', ')',
            '0', '.', '=', '+', '^',
            'sin', 'cos', 'tan'
        ]

        row = 1
        col = 0
        for button in buttons:
            if button == "=":
                tk.Button(root, text=button, width=5, height=2, font=("Arial", 18),
                          command=self.calculate).grid(row=row, column=col)
            elif button == "C":
                tk.Button(root, text=button, width=5, height=2, font=("Arial", 18),
                          command=self.clear).grid(row=row, column=col)
            elif button in ["sin", "cos", "tan"]:
                tk.Button(root, text=button, width=5, height=2, font=("Arial", 18),
                          command=lambda b=button: self.append_function(b)).grid(row=row, column=col)
            else:
                tk.Button(root, text=button, width=5, height=2, font=("Arial", 18),
                          command=lambda b=button: self.append(b)).grid(row=row, column=col)
            col += 1
            if col > 4:
                col = 0
                row += 1

    def append(self, char):
        self.expression += str(char)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def append_function(self, func):
        self.expression += func + "("
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            # Safely evaluate the expression
            result = eval(self.expression, {"sin": sine, "cos": cosine, "tan": tangent,
                                            "pow": pow, "radians": radians})
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            self.expression = str(result)
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
