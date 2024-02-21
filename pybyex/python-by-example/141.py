import sqlite3 as sqlite



# Create authors table



with sqlite.connect("BookInfo.db") as conn:
    cursor = conn.cursor()
    # create authors table
    author_table_sql = """
        CREATE TABLE IF NOT EXISTS author(
            id integer PRIMARY KEY,
            name text,
            place_of_birth text
    );"""

    book_table_sql = """
        CREATE TABLE IF NOT EXISTS book(
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            date_published TEXT
    );"""

    cursor.execute(author_table_sql)
    cursor.execute(book_table_sql)

authors = [
    (1, "Agatha Chrisite", "Torquay"),
    (2, "Cecelia Ahern", "Dublin"),
    (3, "J.K. Rowling", "Bristol"),
    (4, "Oscar Wilde", "Dublin")
]


books = [
    (1, "De Profundis", "Oscar Wilde", "1905"),
    (2, "Harry Potter and the chamber of secretes", "J.K. Rowlling", "1998"),
    (3, "Harry Potter and the prisoner of Azkaban", "J.K. Rowlling", "1999"),
    (4, "Lyrebird", "Cecelia Ahern", "2017")
]


# Insert authors and books to the db

with sqlite.connect("BookInfo.db") as conn:
    cursor = conn.cursor()
    author_insert_sql = """ INSERT INTO author(id, name, palce_of_birth)
                            VALUES (?, ?, ?); """
    for author in authors:
        cursor.execute(author_insert_sql, author)

    book_insert_sql = """ INSERT INTO book(id, title, author, date_published)
                          VALUES (?, ?, ?, ?); """
    for book in books:
        cursor.execute(book_insert_sql, book)

print("Date saved!")


