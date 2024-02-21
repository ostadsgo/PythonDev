import tkinter as tk
from tkinter import ttk

def show_result():
    result["text"] = name.get() + ", " + gender_var.get()
root = tk.Tk()
root.title("Challenage 136")

gender_var = tk.StringVar()
name = ttk.Entry(root)
gender = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Fmale"])
name.pack()
gender.pack()
result = ttk.Label(root)
result.pack()
ttk.Button(root, text="Show", command=show_result).pack()

root.mainloop()
