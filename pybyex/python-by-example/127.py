import tkinter as tk
from tkinter import ttk


def add_name():
    new_name = name.get()
    names_list = names["text"]
    names_list = names_list + new_name + "\n"
    names["text"] = names_list

def clear_name_list():
    names["text"] = ""

root = tk.Tk()
names = ttk.Label(root, text="")
names.pack()
name = ttk.Entry(root)
name.pack()
ttk.Button(root, text="Add to list", command=add_name).pack()
ttk.Button(root, text="Clear name list", command=clear_name_list).pack()
root.mainloop()
