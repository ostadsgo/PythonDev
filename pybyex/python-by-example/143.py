import sqlite3



year = input("Enter a year to see all published book on that year: ")

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()
    sql = """ SELECT title, date_published FROM book
              WHERE date_published >= ?
              ORDER BY date_published;
          """
    cursor.execute(sql, (year,))
    data = cursor.fetchall()

for item in data:
    print(item[1], item[0])
