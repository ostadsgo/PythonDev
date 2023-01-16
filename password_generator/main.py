from random import choices
import tkinter as tk
from tkinter import ttk


class MainFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        #  random generated password
        self.password_len = tk.IntVar()
        self.password = tk.StringVar()
        self.upper = tk.BooleanVar()
        self.lower = tk.BooleanVar()
        self.number = tk.BooleanVar()
        self.symbol = tk.BooleanVar()
        self.lowers = "".join(chr(i) for i in range(97, 123))
        self.uppers = "".join(ch.upper() for ch in self.lowers)
        self.numbers = "".join(chr(i) for i in range(48, 58))
        self.symbols = "@!#$%&^()*+"

        password_frame = ttk.Frame(self, relief=tk.SOLID, padding=(5, 10))
        password_frame.pack(expand=True, fill=tk.BOTH, pady=(0, 10))

        password_entry = ttk.Entry(password_frame, width=50, textvariable=self.password)
        copy_button = ttk.Button(
            password_frame, text="Copy", command=self.copy_password
        )
        password_entry.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        copy_button.pack(expand=True, fill=tk.BOTH, padx=(10, 0))

        # Settings for password
        setting_frame = ttk.Frame(self, relief=tk.SOLID, padding=(5, 10))
        setting_frame.pack(expand=True, fill=tk.BOTH)

        # settings
        uppercase_checkbutton = ttk.Checkbutton(
            setting_frame, variable=self.upper, text="Uppercase"
        )
        lowercase_checkbutton = ttk.Checkbutton(
            setting_frame, variable=self.lower, text="Lowercase"
        )
        number_checkbutton = ttk.Checkbutton(
            setting_frame, variable=self.number, text="Numbers"
        )
        symbol_checkbutton = ttk.Checkbutton(
            setting_frame, variable=self.symbol, text="Symbols"
        )
        passwrod_len_label = ttk.Label(setting_frame, text="Password Length")
        password_len_entry = ttk.Entry(setting_frame, textvariable=self.password_len)
        generate_password_button = ttk.Button(
            self, text="Generate Password", command=self.generate_password
        )
        self.password_len.set(12)
        uppercase_checkbutton.pack(expand=True, fill=tk.BOTH)
        lowercase_checkbutton.pack(expand=True, fill=tk.BOTH)
        symbol_checkbutton.pack(expand=True, fill=tk.BOTH)
        number_checkbutton.pack(expand=True, fill=tk.BOTH)
        passwrod_len_label.pack(expand=True, fill=tk.BOTH)
        password_len_entry.pack(expand=True, fill=tk.BOTH)
        generate_password_button.pack(expand=True, fill=tk.BOTH)

    def copy_password(self):
        print("copy password to clipboard")

    def generate_password(self):
        n = self.password_len.get()
        if self.upper.get():
            self.password.set("".join(choices(self.uppers, k=n)))


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        mainframe = MainFrame(self, padding=(5, 10))
        mainframe.pack(expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    app = App()
    app.mainloop()
