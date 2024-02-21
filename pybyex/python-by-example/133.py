import tkinter as tk
from tkinter import ttk

def greeting():
   greet.insert(0, "Hello " + name.get()) 
root = tk.Tk()
root.title("Hello to You")

image = tk.PhotoImage(file="catkeyboard.gif")
label = ttk.Label(image=image)
label.image = image
label.pack()
name = ttk.Entry(root)
name.pack()
ttk.Button(root, text="Press Me", command=greeting).pack()
greet = ttk.Entry(root)
greet.pack()


root.mainloop()
