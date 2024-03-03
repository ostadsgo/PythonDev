import tkinter as tk
from tkinter import ttk


def calculate(mile_val, km_val):
    miles = mile_val.get()
    km = round(miles * 1.6, 2)
    km_val.set(km)


def main():
    root = tk.Tk()

    root.title("Convert Mile to KM")
    root.minsize(width=300, height=150)

    mile_val = tk.IntVar()
    km_val = tk.IntVar()
    window = ttk.Frame(root, relief="sunken", padding=(5, 10))
    window.pack(expand=True, fill=tk.BOTH)

    # row 0
    mile_entry = ttk.Entry(window, textvariable=mile_val, width=10)
    mile_entry.grid(row=0, column=1)
    ttk.Label(window, text="Miles").grid(row=0, column=2)

    # row 1
    ttk.Label(window, text="is equal to").grid(row=1, column=0)
    result_label = ttk.Label(window, text="is equal to", textvariable=km_val)
    result_label.grid(row=1, column=1)
    ttk.Label(window, text="Km").grid(row=1, column=2)

    # button
    calculate_button = ttk.Button(
        window, text="Calculate", command=lambda: calculate(mile_val, km_val)
    )
    calculate_button.grid(row=2, column=1)

    for child in window.winfo_children():
        child.grid_configure(padx=5, pady=5, sticky="e")

    window.mainloop()


if __name__ == "__main__":
    main()
