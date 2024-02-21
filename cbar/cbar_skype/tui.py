#Import the required library
from tkinter import *
from tkinter import ttk

#Create an instance of tkinter frame
win = Tk()
win.title("Application to represent the Programming Languages ")

#Set the geometry
win.geometry("600x200")

#Create a label
ttk.Label(win, text ="Treeview(hierarchical)").pack()

#Treeview List Instantiation
treeview = ttk.Treeview(win)
treeview.pack()
treeview.insert('', '0', 'i1', text ='Language')
treeview.insert('', '1', 'i2', text ='FrontEnd')
treeview.insert('', '2', 'i3', text ='Backend')
treeview.insert('i2', 'end', 'HTML', text ='RUBY')
treeview.insert('i2', 'end', 'Python', text ='JavaScript')
treeview.insert('i3', 'end', 'C++', text ='Java')
treeview.insert('i3', 'end', 'RUST', text ='Python')
treeview.move('i2', 'i1', 'end')
treeview.move('i3', 'i1', 'end')
treeview.move('i2', 'i1', 'end')

win.mainloop()
