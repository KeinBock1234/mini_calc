import tkinter as tk
from tkinter import ttk


def calculate(op):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        if op == '+':
            result.set(a + b)
        elif op == '-':
            result.set(a - b)
        elif op == '*':
            result.set(a * b)
        elif op == '/':
            result.set(a / b if b != 0 else "Fehler: ÷0")
    except ValueError:
        result.set("Ungültige Eingabe")


# ==============================
# Hauptfenster
# ==============================
root = tk.Tk()
root.title("Mini-Rechner")
root.geometry("320x220")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

# ==============================
# Styles (modern)
# ==============================
style = ttk.Style()
style.theme_use("default")

style.configure(
    "TButton",
    font=("Segoe UI", 12),
    padding=6
)

style.configure(
    "Operator.TButton",
    background="#4CAF50"
)

style.configure(
    "TEntry",
    font=("Segoe UI", 12)
)

# ==============================
# Eingabebereich
# ==============================
frame_input = tk.Frame(root, bg="#f4f4f4")
frame_input.pack(pady=15)

entry_a = ttk.Entry(frame_input, width=12)
entry_b = ttk.Entry(frame_input, width=12)

entry_a.grid(row=0, column=0, padx=5)
entry_b.grid(row=0, column=1, padx=5)

# ==============================
# Ergebnisanzeige
# ==============================
result = tk.StringVar()

label_result = tk.Label(
    root,
    textvariable=result,
    font=("Segoe UI", 14, "bold"),
    bg="#ffffff",
    relief="solid",
    height=2,
    width=22
)
label_result.pack(pady=10)

# ==============================
# Button-Bereich
# ==============================
frame_buttons = tk.Frame(root, bg="#f4f4f4")
frame_buttons.pack(pady=10)

operators = ['+', '-', '*', '/']

for i, op in enumerate(operators):
    ttk.Button(
        frame_buttons,
        text=op,
        width=5,
        command=lambda o=op: calculate(o)
    ).grid(row=0, column=i, padx=5)

# ==============================
# Start
# ==============================
root.mainloop()
