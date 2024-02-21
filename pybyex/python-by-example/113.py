import csv


records = []
ans = "y"
while ans == "y":
    name = input("Enter a book name: ")
    author = input("Enter the author name: ")
    year = input("Enter the release year: ")
    ans = input("Would you like add another book (y/n): ")
    book = (name, author, year)
    records.append(book)

file = open("Books.csv", "a")
for record in records:
    book = ",".join(record)
    file.write(book + "\n")

file.close()

u_author = input("Enter author name: ")
file = open("Books.csv", "r")
reader = csv.reader(file)
books = list(reader)

for row in books:
    name, author, year = row
    if author == u_author:
        print(row)

file.close()
