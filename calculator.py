import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.expression = ""

        # Поле для ввода и вывода
        self.entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=2, relief="solid", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # Создание кнопок
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 1, 4)
        ]

        for button in buttons:
            text, row, col = button[0], button[1], button[2]
            colspan = button[3] if len(button) > 3 else 1
            btn = tk.Button(root, text=text, font=("Arial", 14), width=5, height=2,
                            command=lambda x=text: self.button_click(x))
            btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="ew")

    def button_click(self, char):
        if char == 'C':
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