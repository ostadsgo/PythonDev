import tkinter as tk

from tkinter import ttk


def calculate():
    try:
        equation.set(eval(equation.get()))
    except ZeroDivisionError:
        equation.set("Number cannot divided by zero.")
    except Exception:
        equation.set("Number cannot divided by zero.")


def set_key(event=None):
    # callect all text inside the entry and make the equation
    equ = equation.get() + str(event.widget["text"])
    equation.set(equ)


def clear_one():
    equation.set(equation.get()[:-1])


def clear_all():
    equation.set("")


def on_enter(event):
    calculate()


root = tk.Tk()
root.title("Tkinter Calculator")
root.geometry("270x320")
mainframe = ttk.Frame(root, padding=10)
mainframe.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))

equation = tk.StringVar()
output = ttk.Entry(mainframe, textvariable=equation, font="Calibri 15")
output.grid(row=0, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.S, tk.N), pady=5)

d = {"C": clear_one, "CC": clear_all}
col = 0
for item, func in d.items():
    ttk.Button(mainframe, text=item, command=func).grid(
        row=1, column=col, sticky=(tk.W, tk.E, tk.S, tk.N)
    )
    col += 1

col = 2
for item in ["**", "/"]:
    b = ttk.Button(mainframe, text=item)
    b.grid(row=1, column=col, sticky=(tk.W, tk.E, tk.S, tk.N))
    b.bind("<Button-1>", set_key)
    col += 1

row = 2
col = 0
for num in range(9, 0, -1):
    if col >= 3:
        row += 1
        col = 0
    b = ttk.Button(mainframe, text=num)
    b.grid(row=row, column=col, sticky=(tk.W, tk.E, tk.S, tk.N))
    b.bind("<Button-1>", set_key)
    col += 1

row = 2
for item in ["*", "-", "+"]:
    b = ttk.Button(mainframe, text=item)
    b.grid(row=row, column=3, sticky=(tk.W, tk.E, tk.S, tk.N))
    b.bind("<Button-1>", set_key)
    row += 1


col = 0
for item in ["0", ".", "="]:
    if item == "=":
        ttk.Button(mainframe, text=item, command=calculate).grid(
            row=5, column=col, columnspan=2, sticky=(tk.W, tk.E, tk.S, tk.N)
        )
    else:
        b = ttk.Button(mainframe, text=item)
        b.grid(row=5, column=col, sticky=(tk.W, tk.E, tk.S, tk.N))
        b.bind("<Button-1>", set_key)
    col += 1

# Events
output.bind("<Return>", on_enter)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

row_size, column_size = mainframe.grid_size()
for col_number in range(0, row_size):
    mainframe.columnconfigure(col_number, weight=1)
for row_number in range(0, column_size):
    mainframe.rowconfigure(row_number, weight=1)


root.mainloop()
