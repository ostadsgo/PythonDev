import sqlite3 as sqlite



def get_connection_cursor(db_name):
    with sqlite.connect(db_name) as conn:
        cur = conn.cursor()
        return conn, cur

def display_authors_info(db_name):
    sql = """ SELECT name, place_of_birth
              FROM author;
          """

    conn, cursor = get_connection_cursor(db_name)
    cursor.execute(sql)
    authors = cursor.fetchall()
    return authors


def get_authors_name(birth_place):
    conn, cur = get_connection_cursor("BookInfo.db")
    author_name_sql = """ SELECT name
                          FROM author
                          WHERE place_of_birth=?;
                      """
    cur.execute(author_name_sql, (birth_place,))
    authors_name = cur.fetchall()
    return authors_name

def get_books(author):
    _, cur = get_connection_cursor("BookInfo.db")
    sql = """ SELECT title, date_published
              FROM book
              WHERE author=?;
          """
    cur.execute(sql, author)
    return cur.fetchall()


def main():
    authors = display_authors_info("BookInfo.db")
    max_len_name = len(max(authors, key=lambda pair: len(pair[0]))[0])
    name = "Name"
    header = f"{name:{max_len_name}} Place of Birth"
    print(header)
    for author in authors:
        name, birth = author
        output = f"{name:{max_len_name}} {birth}"
        print(output)

    birth_place = input("Enter a birth place: ")
    authors = get_authors_name(birth_place)
    for author in authors:
        books = get_books(author)
        if books:
            for book in books:
                print(book)
        else:
            print("The author desn't have any registerd book.")

if __name__ == "__main__":
    main()
