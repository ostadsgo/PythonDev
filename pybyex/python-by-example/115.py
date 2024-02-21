import csv

file = open("Books.csv", "r")
reader = csv.reader(file)
next(reader)
index = 1
for row in list(reader):
    print(index, row)
    index += 1
