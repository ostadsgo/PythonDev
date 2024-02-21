

name = input("Enter a book name: ")
author = input("Enter the author name: ")
year = input("Enter the years of release: ")
book = (name, author, year)
record = ",".join(book)

file = open("Books.csv", "a")
file.write(record + "\n")
file.close()

file = open("Books.csv", "r")
for row in file:
    print(row, end="")
file.close()

