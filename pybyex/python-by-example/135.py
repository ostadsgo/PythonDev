import tkinter as tk
from tkinter import ttk



def change_color():
    color = colorbox.get().lower()
    style.configure("TButton", background=color)

root = tk.Tk()
root.title("Button Color Change")
style = ttk.Style()
style.configure("TButton", background="red")
color_var = tk.StringVar()
color_var.set("Red")
colorbox = ttk.Combobox(root, values=["Red", "Blue", "Green", "Black"], textvariable=color_var)
colorbox.pack()
ttk.Button(root, text="Change color", command=change_color, style="TButton").pack()

root.mainloop()
