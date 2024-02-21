import tkinter as tk
from tkinter import ttk

from random import randint

def run():
    label.config(text=randint(1, 6))

root = tk.Tk()

label = ttk.Label(root, text="")
label.pack()
ttk.Button(root, text="Press Me", command=run).pack()

root.mainloop()
