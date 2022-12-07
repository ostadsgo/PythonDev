import tkinter as tk
from tkinter import ttk


class MainFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        #  random generated password
        self.password = tk.StringVar()
        self.password_frame = ttk.Frame(self, relief=tk.SOLID, padding=(5, 10))
        self.password_frame.pack(expand=True, fill=tk.BOTH, pady=(0, 10))

        self.password_entry = ttk.Entry(
            self.password_frame, width=50, textvariable=self.password
        )
        self.copy_button = ttk.Button(
            self.password_frame, text="Copy", command=self.copy_password
        )
        self.password_entry.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        self.copy_button.pack(expand=True, fill=tk.BOTH, padx=(10, 0))

        # Settings for password
        self.setting_frame = ttk.Frame(self, relief=tk.SOLID, padding=(5, 10))
        self.setting_frame.pack(expand=True, fill=tk.BOTH)

        # settings
        self.uppercase_checkbutton = ttk.Checkbutton(
            self.setting_frame, text="Uppercase"
        )
        self.lowercase_checkbutton = ttk.Checkbutton(
            self.setting_frame, text="Lowercase"
        )
        self.symbol_checkbutton = ttk.Checkbutton(self.setting_frame, text="Symbols")
        self.number_checkbutton = ttk.Checkbutton(self.setting_frame, text="Numbers")
        self.uppercase_checkbutton.pack(expand=True, fill=tk.BOTH)
        self.lowercase_checkbutton.pack(expand=True, fill=tk.BOTH)
        self.symbol_checkbutton.pack(expand=True, fill=tk.BOTH)
        self.number_checkbutton.pack(expand=True, fill=tk.BOTH)

        self.generate_password_button = ttk.Button(
            self, text="Generate Password", command=self.generate_password
        )
        self.generate_password_button.pack(expand=True, fill=tk.BOTH)

    def copy_password(self):
        print("copy password to clipboard")

    def generate_password(self):
        print("Generate password.")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        mainframe = MainFrame(self, padding=(5, 10))
        mainframe.pack(expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    app = App()
    app.mainloop()
