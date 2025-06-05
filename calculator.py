import tkinter as tk

# Создание основного окна
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Поле для ввода и вывода
entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Создание кнопок с цифрами
buttons = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0'
]

row = 1
col = 0
for button_text in buttons:
    btn = tk.Button(root, text=button_text, font=("Arial", 14), width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 2:
        col = 0
        row += 1

# Запуск приложения
root.mainloop()