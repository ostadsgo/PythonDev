books = [
    ("books", "author", "year release"),
    ("To Kill A Mockingbird", "Harper Lee", "1960"),
    ("a breif history of time", "Stephen Hawking", "1988"),
    ("The Great Gatsby", "F. Scott Fitzgerald", "1922"),
    ("The Man Who Mistook His Wife for a Hat", "Oliver Sacks", "1985"),
    ("Pride and Prejudice", "Jane Austen", "1813"),
]

file = open("Books.csv", "w")
for book in books:
    row = ','.join(book)
    file.write(row + "\n")
file.close()
