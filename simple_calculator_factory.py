import tkinter as tk
from abc import ABC, abstractmethod

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
        else:
            raise ValueError(f"Unknown button type: {button_type}")

# Основной класс калькулятора (пока пустой)
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator Factory")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

# Запуск приложения
if name == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()