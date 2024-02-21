# There is duplication in create_table_* methods!!!
# I need to use with statement to avoid conn.close()


import sqlite3
import tkinter as tk

from sqlite3 import Error
from tkinter import ttk




class Database:
    def __init__(self, dbname):
        self.dbname = dbname

    def _connect(self):
        conn = None
        try:
            conn = sqlite3.connect(self.dbname)
            return conn
        except Error as e:
            print("Error in connection::", e)
        

    def create_artist_table(self):
        sql = """ CREATE TABLE IF NOT EXISTS artists (
                  id integer PRIMARY KEY,
                  name text,
                  address text,
                  town text,
                  country text,
                  postcode text
              );
              """
        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
        except Error as e: 
            print("Error in create table::", e) 
        finally:
            conn.close()

    def create_price_of_art_table(self):
        sql = """ CREATE TABLE IF NOT EXISTS price_of_art (
                  id INTEGER PRIMARY KEY,
                  artist_id INTEGER NOT NULL,
                  title TEXT,
                  meidum TEXT,
                  price REAL,
                  FOREIGN KEY (artist_id) REFERENCES artists (id)
              );
              """
        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
        except Error as e:
            print(e)
        finally:
            conn.close()
    def create_artist(self, *record):
        sql = """ INSERT INTO artists(
                      name, address, town, 
                      country, postcode
                  )
                  VALUES(?, ?, ?, ?, ?);
              """
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(sql, record)
        conn.commit()
        print("Artist saved.")

    def read_all_arts(self):
        sql = """ SELECT *
                  FROM price_of_art;
              """
        conn = self._connect()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Error as e:
            print(e)
        finally:
            conn.close()

    def get_artist_name_by_id(self, artist_id):
        sql = """ SELECT name 
                  FROM artists
                  WHERE id=?
        """

        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(sql, [artist_id])
            return cur.fetchone()[0]
        except Error as e:
            print(e)
        finally:
            conn.close()

    def delete_art_by_id(self, art_id):
        sql = """ DELETE FROM price_of_art
                  WHERE id=?
              """
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(sql, [art_id])
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()
    
    def search_by_price(self, price):
        sql = """ SELECT *
                  FROM price_of_art
                  WHERE price=?
              """
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(sql, [price])
            return cur.fetchall()
        except Error as e:
            print(e)
        finally:
            conn.close()




class ArtGallery:
    def __init__(self, db):
        self.db = db
        self.root = tk.Tk()
        self.root.title("Art Gallery")
        
        frame = ttk.Frame(self.root)
        frame.pack(fill='x', expand=True)
        add_artist = ttk.Button(frame, text="New Artist")
        show_arts_btn = ttk.Button(frame, text="Show all arts")
        add_artist["command"] = self.add_new_artist
        add_artist.pack(side="left", fill='x', expand=True)
        show_arts_btn.pack(fill='x', expand=True)
        arts_listbox = tk.Listbox(self.root)
        arts_listbox.pack(expand=True, fill="both")
        show_arts_btn["command"] = lambda: self.display_arts(arts_listbox)
        self.search_by_price()
        self.sell(arts_listbox)
        self.display_arts(arts_listbox)
        self.root.mainloop()

    def search_by_price(self):
        frame = ttk.Frame()
        search_box = ttk.Entry(frame)
        search_box.pack(side="left", expand=True, fill='x')
        search_btn = ttk.Button(frame, text="Search by price")
        search_btn.pack(padx=(10, 0))
        frame.pack(expand=True, fill='x')
        search_btn["command"] = lambda: self.search(search_box.get())

    def search(self, price):
        result = self.db.search_by_price(price)
        found_arts = [] 
        for art in result:
            artist_name = self.db.get_artist_name_by_id(art[1])
            s = f"{art[0]}. {artist_name}, {art[1]} {art[2]} {art[3]} ${art[4]} "
            found_arts.append(s)
        self.arts_var.set(found_arts)
    
    def add_new_artist(self):
        window = tk.Toplevel(self.root)
        ttk.Label(window, text="Name: ").pack()
        name = ttk.Entry(window)
        name.pack()
        ttk.Label(window, text="Address").pack()
        addr = ttk.Entry(window)
        addr.pack()
        ttk.Label(window, text="Town").pack()
        town = ttk.Entry(window)
        town.pack()
        ttk.Label(window, text="Country").pack()
        country = ttk.Entry(window)
        country.pack()
        ttk.Label(window, text="Postcode").pack()
        postcode = ttk.Entry(window)
        postcode.pack()
        save_btn = ttk.Button(window, text="Save Artist")
        save_btn.pack()
        save_btn["command"] = lambda: self.db.create_artist(
                name.get(), 
                addr.get(), 
                town.get(),
                country.get(), 
                postcode.get()
            )
    
    def sold(self, listbox, art_ids):
        selected_item = listbox.curselection()[0]
        all_arts = listbox.get(0, tk.END)
        listbox.delete(selected_item)
        deleted_item = all_arts[selected_item]
        deleted_item_id = art_ids[selected_item]
        # Save sold pices to sold.txt
        with open("sold.txt", "a") as f:
            f.write(deleted_item + "\n")
        # Delete sold pices from art table
        self.db.delete_art_by_id(deleted_item_id)

    def display_arts(self, arts_listbox):
        self.art_ids = []
        art_prices = []
        arts_list = []
        self.arts_var = tk.StringVar(value=arts_list)
        arts_listbox["listvariable"] = self.arts_var

        arts = self.db.read_all_arts()
        for art in arts:
            self.art_ids.append(art[0])
            art_prices.append(art[4])
            artist_name = self.db.get_artist_name_by_id(art[1])
            s = f"{art[0]}. {artist_name}, {art[1]} {art[2]} {art[3]} ${art[4]} "
            arts_list.append(s)

        self.arts_var.set(arts_list)

    def sell(self, arts_listbox):
        sell_btn = ttk.Button(self.root, text="Sell")
        sell_btn.pack(fill="x", expand=True)
        sell_btn.bind("<1>", lambda e: self.sold(arts_listbox, self.art_ids))





        




if __name__ == "__main__":
    ### TEST  ###
    db = Database("art_gallery.db")
    #db.create_artist_table()
    #db.create_price_of_art_table()
    art_gallery = ArtGallery(db)

