#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 14:23:28 2023

@author: a420192
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import table
from force import CBar, CBush
# import matplotlib.pyplot as plt
    
    
class App:
    def __init__(self):
        self.file_paths=[]
    def main(self):
        self.root = tk.Tk()
        self.root.title("Bolt analyser")
        open_file = ttk.Button(self.root, text="open files", command = self.open_files)
        open_file.grid(row=0,column=0)
        
        self.element_box = tk.Listbox(self.root)
        self.tables = []
        
        
        
        self.root.mainloop()
    
    def open_files(self):
        self.file_paths = filedialog.askopenfilenames(initialdir ="/home/saeed/docs/repos/cbar/f06/", title = "Select file",
                        filetypes = (("k file","*.f06"),("all files","*.*")))
        
        # self.file_paths = file_objects
        self.make_subtitle_buttons()
            
    
    
    def extract_subtitle(self,f):
        sub = ""
        with open(f) as file:
            for line in file.readlines():
                if "SUBTITLE=" in line:
                    sub = line.split("SUBTITLE=")[-1]
                    break       
        return sub
    
    def make_subtitle_buttons(self):
        for num, path in enumerate(self.file_paths):
            sub = self.extract_subtitle(path)
            button = ttk.Button(self.root, text = sub + " : " + os.path.basename(path)[:-4], command= lambda: self.get_table(path))
            button.grid(row = num+1, column = 0)
            
            
    def get_table(self, path):
        self.tables =  table.get_tables(path)
        
        for tbl in self.tables:
            element_id = tbl.get("element_id")
            self.element_box.insert(tk.END, element_id)
            self.element_box.bind("<<ListboxSelect>>", self.show_el_cols)
            
        self.element_box.grid(row=0,column=1)
        
        scrollbar = tk.Scrollbar(self.root, command=self.element_box.yview)
        scrollbar.grid(row=0, column=1, sticky="ens")

        # Configure the Listbox to work with the Scrollbar
        self.element_box.config(yscrollcommand=scrollbar.set)
        
        
    def show_el_cols(self,event):
        selected_index = self.element_box.curselection()[0]  # Get the index of the selected item
        selected_item = self.element_box.get(selected_index)  # Get the text of the selected item
        print(selected_item)
        
        for tbl in self.tables:
            
            if tbl.get("element_id") == selected_item.strip():
                if tbl.get("el_type") == "CBUSH":
                    bar = CBush(tbl)
                    
                    self.show_headers(bar)
                elif tbl.get("el_type") == "CBAR":
                    print("it is a cbar")
                    bar = CBar(tbl)
                    self.show_headers(bar)
                    
    def draw_plot(self, event, bar):
        head = event.widget["text"]
        if bar.el_type == "CBUSH":
            head_dict_cbush = {"TIME":bar.time, "FORCE-X":bar.force_x, "FORCE-Y":bar.force_y,
                                "FORCE-Z":bar.force_z,  "MOMENT-X":bar.moment_x,
                                "MOMENT-Y":bar.moment_y, "MOMENT-Z":bar.moment_z,
                                "Total Shear":bar.total_shear}
                 
        
        # y = head_dict_cbush.get(head)
        # x = bar.time
        # plt.figure()
        # plt.plot(x, y, marker='o', linestyle='-', color='b', label='Data')
        # # Add labels and title
        # plt.xlabel('Time')
        # plt.ylabel(head)
        # plt.title(bar.el_type + "_" + "force")
        # # Add a legend
        # plt.legend()
        # # Show the plot
        # plt.show()
                

    def show_headers(self, bar):
        headers = []
        
        if bar.el_type == "CBUSH":
            headers = bar.header

        elif bar.el_type == "CBAR":
            headers = bar.sub_header
            
            
        for num, head in enumerate(headers):
            if head == "TIME":
                continue
            
            
            button = ttk.Button(self.root, text = head)
            button.bind("<Button-1>", lambda event, bar=bar: self.draw_plot(event, bar))
 
            button.grid(row = num+1, column = 3)            
            
            
            
    
if __name__ == "__main__":
    app = App()
    app.main()



