import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        self.expression = ""

        # Поле для ввода и вывода
        self.entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=2, relief="solid", justify="right", bg="#ffffff")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # Создание кнопок
        buttons = [
            ('7', 1, 0, "#ffffff"), ('8', 1, 1, "#ffffff"), ('9', 1, 2, "#ffffff"), ('/', 1, 3, "#d9e6ff"),
            ('4', 2, 0, "#ffffff"), ('5', 2, 1, "#ffffff"), ('6', 2, 2, "#ffffff"), ('*', 2, 3, "#d9e6ff"),
            ('1', 3, 0, "#ffffff"), ('2', 3, 1, "#ffffff"), ('3', 3, 2, "#ffffff"), ('-', 3, 3, "#d9e6ff"),
            ('0', 4, 0, "#ffffff"), ('.', 4, 1, "#ffffff"), ('C', 4, 2, "#ffcccc"), ('+', 4, 3, "#d9e6ff"),
            ('=', 5, 0, "#b3d9ff", 4)
        ]

        for button in buttons:
            text, row, col, bg = button[0], button[1], button[2], button[3]
            colspan = button[4] if len(button) > 4 else 1
            btn = tk.Button(root, text=text, font=("Arial", 14), width=5, height=2, bg=bg, activebackground="#e0e0e0",
                            command=lambda x=text: self.button_click(x))
            btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="ew")

    def button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                result = eval(self.expression)
                self.expression = str(result)
            except ZeroDivisionError:
                messagebox.showerror("Error", "Division by zero!")
                self.expression = ""
            except:
                messagebox.showerror("Error", "Invalid expression!")
                self.expression = ""
        elif char in '0123456789.':
            self.expression += char
        elif char in '+-*/':
            if self.expression and self.expression[-1] not in '+-*/':
                self.expression += char
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

# Запуск приложения
root = tk.Tk()
app = Calculator(root)
root.mainloop()