import tkinter as tk
from tkinter import ttk

def to_mile():
    km_value = int(km.get())
    mile_label["text"] = km_value * 1.6093 

def to_km():
    mile_val = int(mile.get())
    km_label["text"] = mile_val * .6214

root = tk.Tk()
km = ttk.Entry(root)
km.pack()
ttk.Button(root, text="Convert To Mile", command=to_mile).pack()
mile_label = ttk.Label(root, text="")
mile_label.pack()

mile = ttk.Entry()
mile.pack()
ttk.Button(root, text="Convert To KM", command=to_km).pack()
km_label = ttk.Label(root)
km_label.pack()

root.mainloop()
