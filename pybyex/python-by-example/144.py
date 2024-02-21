import sqlite3 as sqlite



author_name = input("Enter author name: ")

with sqlite.connect("BookInfo.db") as db:
    cursor = db.cursor()
    sql = """ SELECT * FROM book
              WHERE author=?;
          """
    cursor.execute(sql, (author_name,))
    data = cursor.fetchall()

print(data)
with open("books.txt", "w") as book_file:
    for record in data:
        row = "-".join(str(x) for x in record)
        book_file.write(row + "\n")

