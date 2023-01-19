import time
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image
import brain_stretch as brain

# IDEA:
# keep log of all incorect equations you can analysis them.


class Header(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.brain_image = ImageTk.PhotoImage(Image.open("brain3.jpg"))
        ttk.Label(self, image=self.brain_image).pack()


class Timer(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.minutes = 0
        self.seconds = 0
        style = ttk.Style()
        style.configure("timer.TLabel", foreground="#6e1d60", font=("Roboto Mono", 14))
        self.timer = ttk.Label(self, text="00:00", style="timer.TLabel")
        self.timer.pack()
        self.update_timer()

    def update_timer(self):
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1
        self.seconds += 1
        # time.sleep(1)
        self.timer["text"] = f"{self.minutes:0>2}:{self.seconds:0>2}"
        self.master.after(1000, self.update_timer)


class BrainStretch(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.style = ttk.Style(self)
        self.style.configure("TLabel", font=("Roboto Mono", 14), foreground="#121111")
        self.style.configure("correct.TLabel", foreground="#127a14")
        self.style.configure("wrong.TLabel", foreground="#96121d")
        # widgets
        self.question = ttk.Label(self, text=brain.get_question("+"))
        self.responsebox = ttk.Entry(self, font=("Roboto Mono", 14))
        self.log = ttk.Label(self, text="Result")
        # pack and configs
        self.question.pack()
        self.responsebox.pack()
        self.log.pack()
        self.responsebox.focus()
        # binds
        self.responsebox.bind("<Return>", self.evaluate_question)

        # styling
        for child in self.winfo_children():
            child.pack_configure(padx=5, pady=5)

    def create_question(self):
        self.question["text"] = brain.get_question("+")

    def evaluate_question(self, event):
        question = self.question["text"]
        answer = brain.calculate(question)
        response = int(self.responsebox.get())
        if brain.compare(response, answer):
            self.log["text"] = f"CORRECT"
            self.log["style"] = "correct.TLabel"
        else:
            self.log["text"] = f"WRONG"
            self.log["style"] = "wrong.TLabel"
            num1, num2 = question.split("+")
            row = [int(num1.strip()), int(num2.strip()), "+", response, answer]
            brain.save_mistakes(row)
        self.responsebox.delete(0, tk.END)
        self.create_question()


class MainFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Header
        header = Header(self)
        header.grid(row=0, column=0)

        # Timer
        timer = Timer(self)
        timer.grid(row=1, column=0)

        # Question / Answer / Result
        brain_stretch = BrainStretch(self)
        brain_stretch.grid(row=2, column=0)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Brain Stertch")
        # ui
        mainframe = MainFrame(self)
        mainframe.pack(expand=True, fill=tk.BOTH)

        self.mainloop()


if __name__ == "__main__":
    App()
