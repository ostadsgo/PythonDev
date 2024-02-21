import sqlite3 as sqlite



contacts = [
    {"first_name": "Simon", "surname": "Howels", "phone_number": "09134658711"},
    {"first_name": "Joe", "surname": "Philips", "phone_number": "09123331100"},
    {"first_name": "Karen", "surname": "Smith", "phone_number": "09149803311"},
    {"first_name": "Anee", "Jones": "Smith", "phone_number": "09451113300"},
    {"first_name": "Mark", "Manson": "Smith", "phone_number": "09124448901"},
]

fields = tuple(contacts[0].keys())
# sql command to create table
create_table = """CREATE TABLE IF NOT EXISTS phonebook(
                        id INTEGER PRIMARY KEY,
                        {} TEXT,
                        {} TEXT,
                        {} TEXT
                    );""".format(*fields)

with sqlite.connect("phonebook.db") as connection:
    cursor = connection.cursor()
    cursor.execute(create_table)

# sql command to insert a row in the phonebook table
insert_contact_sql = """INSERT INTO phonebook ({}, {}, {})
                        VALUES (?, ?, ?);""".format(*fields)

with sqlite.connect("phonebook.db") as connection:
    cursor = connection.cursor()
    for contact in contacts:
        row = tuple(contact.values())
        cursor.execute(insert_contact_sql, row) 
