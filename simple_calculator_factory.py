import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import messagebox

# Абстрактный класс для кнопок
class Button(ABC):
    @abstractmethod
    def press(self):
        pass

# Конкретные классы кнопок
class DigitButton(Button):
    def __init__(self, digit):
        self._digit = digit

    def press(self):
        return str(self._digit)

class OperatorButton(Button):
    def __init__(self, operation):
        self._operation = operation

    def press(self):
        return self._operation

class ClearButton(Button):
    def press(self):
        return "C"

class EqualsButton(Button):
    def press(self):
        return "="

# Фабрика для создания кнопок
class ButtonFactory:
    @staticmethod
    def create_button(button_type, value=None):
        if button_type == "digit":
            return DigitButton(value)
        elif button_type == "operator":
            return OperatorButton(value)
        elif button_type == "clear":
            return ClearButton()
        elif button_type == "equals":
            return EqualsButton()
        else:
            raise ValueError(f"Unknown button type: {button_type}")

# Основной класс калькулятора
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator Factory")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        self.expression = ""
        self.button_instances = []

        # Поле для ввода и вывода
        self.entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=2, relief="solid", justify="right", bg="#ffffff")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # Создание кнопок через фабрику
        buttons = [
            ("digit", "7", 1, 0, "#ffffff"), ("digit", "8", 1, 1, "#ffffff"), ("digit", "9", 1, 2, "#ffffff"), ("operator", "/", 1, 3, "#d9e6ff"),
            ("digit", "4", 2, 0, "#ffffff"), ("digit", "5", 2, 1, "#ffffff"), ("digit", "6", 2, 2, "#ffffff"), ("operator", "*", 2, 3, "#d9e6ff"),
            ("digit", "1", 3, 0, "#ffffff"), ("digit", "2", 3, 1, "#ffffff"), ("digit", "3", 3, 2, "#ffffff"), ("operator", "-", 3, 3, "#d9e6ff"),
            ("digit", "0", 4, 0, "#ffffff"), ("digit", ".", 4, 1, "#ffffff"), ("clear", "C", 4, 2, "#ffcccc"), ("operator", "+", 4, 3, "#d9e6ff"),
            ("equals", "=", 5, 0, "#b3d9ff", 4)
        ]

        for btn_type, value, row, col, bg in buttons:
            button = ButtonFactory.create_button(btn_type, value)
            self.button_instances.append(button)
            tk_btn = tk.Button(root, text=value, font=("Arial", 14), width=5, height=2, bg=bg, activebackground="#e0e0e0",
                               command=lambda x=button: self.button_click(x))
            tk_btn.grid(row=row, column=col, columnspan=4 if btn_type == "equals" else 1, padx=5, pady=5, sticky="ew")

    def button_click(self, button):
        action = button.press()
        if action == "C":
            self.expression = ""
        elif action == "=":
            try:
                result = eval(self.expression)
                self.expression = str(result)
            except ZeroDivisionError:
                messagebox.showerror("Error", "Division by zero!")
                self.expression = ""
            except:
                messagebox.showerror("Error", "Invalid expression!")
                self.expression = ""
        elif action in "0123456789.":
            self.expression += action
        elif action in "+-*/":
            if self.expression and self.expression[-1] not in "+-*/":
                self.expression += action
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

# Запуск приложения
if name == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()