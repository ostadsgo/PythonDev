import csv
import tkinter as tk

from tkinter import ttk



def save():
    filename = filename_entry.get()
    row = [name_entry.get(), age_entry.get()]
    with open(filename,  'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(row)

root = tk.Tk()
filename_entry = ttk.Entry(root)
filename_entry.pack()
name_entry = ttk.Entry(root)
age_entry = ttk.Entry(root)
name_entry.pack()
age_entry.pack()

ttk.Button(root, text="Save to CSV", command=save).pack()

root.mainloop()
