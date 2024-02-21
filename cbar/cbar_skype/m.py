import tkinter as tk
root = tk.Tk()

# Create a menubar
test_menu = tk.Menu(root)

main_menu = tk.Menu(test_menu, tearoff=False)
# sub_menu.add_command(label='Submenu item 1')
# sub_menu.add_command(label='Submenu item 2')

test_menu.add_cascade(label = 'Main Menu', menu=main_menu)

sub_sub_menu = tk.Menu(sub_menu, tearoff=False)
sub_sub_menu.add_command(label='1')
sub_sub_menu.add_command(label='2')

sub_menu.add_cascade(label='Sub-sub menu', menu=sub_sub_menu)
root.configure(menu=test_menu)
root.mainloop()
