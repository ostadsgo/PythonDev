import csv

file = open("Books.csv", "r")
reader = csv.reader(file)
next(reader)
books = list(reader)
index = 0
for row in books:
    print(index, row)
    index += 1
file.close()


row_index = int(input("Enter the index of row you want to delete: "))
del books[row_index]

index = 0
for row in books:
    print(index, row)
    index += 1
file.close()

row_index = int(input("Enter row index of the row to change data: "))
book_name = input("Enter the book name: ")
author = input("Enter author name: ")
year = input("Year of the book: ")
record = [book_name, author, year]
books[row_index] = record   # update 

file = open("Books.csv", "w")
writer = csv.writer(file)
for row in books:
    writer.writerow(row)

file.close()

index = 0
for row in books:
    print(index, row)
    index += 1
file.close()
