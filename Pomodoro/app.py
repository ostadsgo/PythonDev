import tkinter as tk
from datetime import datetime
from time import sleep
from tkinter import ttk

from PIL import Image, ImageTk


class MainFrame(ttk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.master = master

        self.timer_var = tk.StringVar()
        self.timer_var.set("25:00")

        ## Widgets
        # image
        image = ImageTk.PhotoImage(Image.open("./pomo.jpeg"))
        self.image_label = ttk.Label(
            self,
            image=image,
            textvariable=self.timer_var,
            compound="center",
            font=("Source Code Pro", 18, "bold"),
            foreground="#756AB6",
        )
        self.image_label.image = image
        # timer
        # buttons
        start_button = ttk.Button(self, text="start")
        reset_button = ttk.Button(self, text="reset")

        ## Pack widgets
        self.image_label.pack(expand=True, fill=tk.BOTH)
        start_button.pack(expand=True, fill=tk.BOTH)
        reset_button.pack(expand=True, fill=tk.BOTH)

        start_button.config(command=self.count_down)
        reset_button.config(command=self.on_reset)

        for child in self.winfo_children():
            child.pack_configure(padx=5, pady=5)

        time_string = self.timer_var.get()
        timer = datetime.strptime(time_string, "%M:%S").time()
        self.minutes = timer.minute
        self.seconds = timer.second

    def count_down(self):
        if self.minutes >= 0:
            self.timer_var.set(f"{self.minutes:0>2}:{self.seconds:0>2}")
            print(self.timer_var.get())
            self.seconds -= 1
            print(self.seconds)
            if self.seconds <= 0:
                self.minutes -= 1
                self.seconds = 60
            self.after(1, self.count_down)
        else:
            self.timer_var.set("00:00")

    def on_reset(self):
        self.minutes = 25
        self.seconds = 0
        self.timer_var.set("25:00")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro App")
        mainframe = MainFrame(self, relief="sunken", padding=(4, 10))
        mainframe.pack(expand=True, fill=tk.BOTH)


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
