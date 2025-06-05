import tkinter as tk

# Создание основного окна
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Поле для ввода и вывода
entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Запуск приложения
root.mainloop()