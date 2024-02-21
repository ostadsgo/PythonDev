import sqlite3 as sqlite


class Database:
    def __init__(self, db_filename):
        self.db_filename = db_filename
        self.db = None

    def _create_connection(self):
        try:
            with sqlite.connect(self.db_filename) as db:
                cursor = db.cursor()
                self.db = db
                return cursor
        except sqlite.Error as e:
            print(e)

    def read_all(self):
        cursor = self._create_connection()
        sql = """Select * FROM phonebook;"""
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def create(self, *args):
        cursor = self._create_connection()
        marks = "?, ?, ?"
        fields = "first_name, surname, phone_number"
        sql = f""" INSERT INTO phonebook ({fields})
                  VALUES ({marks});
              """
        cursor.execute(sql, args)
        self.db.commit()
    
    def search_by(self, surname):
        cursor = self._create_connection()
        sql = """ SELECT * FROM phonebook WHERE surname=?; """ 
        cursor.execute(sql, (surname,)) 
        return cursor.fetchone()

    def delete(self, person_id):
        cursor = self._create_connection()
        sql = """ DELETE FROM phonebook WHERE id=?"""
        cursor.execute(sql, (person_id,))
        self.db.commit()
            

def display_menu():
    print("\033c")
    menu = [
            "View phone book",
            "Add to phone book",
            "Search for surname",
            "Delete person form phone book",
            "Quit"
    ]

    for index, item in enumerate(menu, start=1):
        print(f"[{index}] {item}")


db = Database(db_filename="phonebook.db")

while True:
    display_menu()
    response = input("Enter your selection: ")
    if response == "1":
        contacts = db.read_all()
        for contact in  contacts:
            print(contact)

    elif response == "2":
        first = input("First name: ")
        last = input("Last name: ")
        phone = input("Phone number: ")
        db.create(first, last, phone)
        print("Data saved.")
        
    elif response == "3":
        surname = input("Enter surname to search: ")
        result = db.search_by(surname)
        if result is not None:
            print(result)
        else:
            print("Not Found.")

    elif response == "4":
        person_id = int(input("Enter ID of the person you want to delete: "))
        db.delete(person_id)
        print("Deleted successfuly.")

    elif response == "5":
        break

    else:
        print("You choose the wrong option.")

    input("Press any key to back to menu ...")

