import tkinter as tk

from tkinter import ttk

def add():
    value = int(total["text"])
    total_value = value + int(number.get())
    # set the value to total label
    total["text"] = str(total_value)

def reset_total():
    total.config(text="0")

root = tk.Tk()
total = ttk.Label(root, text="0")
total.pack()
number = ttk.Entry(root)
number.pack()
ttk.Button(root, text="Add", command=add).pack()
reset = ttk.Button(root, text="Reset", command=reset_total)
reset.pack()
root.mainloop()
