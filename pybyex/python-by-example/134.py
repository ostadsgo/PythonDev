import tkinter as tk
from random import randint
from tkinter import ttk


def check_ans():
    if rand_num == int(guess.get()):
        label["text"] = "Correct"
    else:
        label["text"] = "Wrong"

def next_question():
    global rand_num
    guess.delete(0, "end")
    rand_num = randint(10, 50)

root = tk.Tk()
root.title("Guess me")
result_var = tk.StringVar()
rand_num = randint(10, 50)

label = ttk.Label(root, text="I am number between 10, 50 guess me.")
guess = ttk.Entry(root)
label.pack()
guess.pack()
ttk.Button(root, text="Check Answer", command=check_ans).pack()
result = ttk.Label(root, textvariable=result_var)
result.pack()
ttk.Button(root, text="Next quesion", command=next_question).pack()

root.mainloop()
