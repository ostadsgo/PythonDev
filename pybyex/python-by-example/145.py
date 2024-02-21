import sqlite3 as sqlite
import tkinter as tk
from tkinter import ttk


def save_data():
    with sqlite.connect("testscore.db") as db:
        cursor = db.cursor()
        sql = """ INSERT INTO student(name, grade)
                  VALUES (?, ?);
              """
        cursor.execute(sql, (name.get(), grade.get()))
        db.commit()


def clear_fields():
    name.delete(0, 'end')
    grade.delete(0, 'end')

root = tk.Tk()
root.title("Test Scores")

ttk.Label(root, text="Enter student's name: ").grid(row=0, column=0)
ttk.Label(root, text="Enter student's grade: ").grid(row=1, column=0)

name = ttk.Entry(root)
grade = ttk.Entry(root)
name.grid(row=0, column=1)
grade.grid(row=1, column=1)

ttk.Button(root, text="Add", command=save_data).grid(row=2, column=1, sticky='w')
ttk.Button(root, text="Clear", command=clear_fields).grid(row=2, column=1, sticky='e')

for child in root.winfo_children():
    child.grid_configure(padx=10, pady=5)

root.mainloop()
