import tkinter as tk
from tkinter import ttk

def calculate():
    result = ""
    number = int(entry.get())
    for i in range(1, 13):
        result += f"{i} x {number} = {i * number}\n"
    time_table["text"] = result


root = tk.Tk()
root.title("Time Table")
ttk.Label(root, text="Enter a number: ").grid(row=0, column=0)
entry = ttk.Entry(root)
entry.grid(row=0, column=1)
button = ttk.Button(root, text="View Time Table", command=calculate)
button.grid(row=0, column=2)
time_table = ttk.Label(root, text="")


for child in root.winfo_children():
    child.grid_configure(padx=10, pady=10)


root.mainloop()

