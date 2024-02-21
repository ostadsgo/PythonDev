import csv
import tkinter as tk

from tkinter import ttk


def add_to_list():
    num = number.get()
    if num.isdigit():
        numbers.append(num)
    output = ','.join(numbers)
    numbers_list_var.set(output) 

def reset():
    global numbers
    numbers = []
    numbers_list_var.set("")
    
def save_csv():
    with open("num_list.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(numbers)
        print("CSV file saved.")

numbers = []
root = tk.Tk()
numbers_list_var = tk.StringVar()
number_list = ttk.Label(root, textvariable=numbers_list_var)
number_list.pack()
number = ttk.Entry(root)
number.pack()
ttk.Button(root, text="Add To List", command=add_to_list).pack()
ttk.Button(root, text="Reset", command=reset).pack()
ttk.Button(root, text="Save to CSV", command=save_csv).pack()

root.mainloop()
