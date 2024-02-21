import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def call():
    x = messagebox.showinfo("Message", f"Hello, {name.get()}")
    print(dir(x))

root = tk.Tk()
ttk.Label(text="Enter your name: ").pack()
name = ttk.Entry(root)
name.pack()
press = ttk.Button(root, text="Press Me", command=call)
press.pack()


root.mainloop()
