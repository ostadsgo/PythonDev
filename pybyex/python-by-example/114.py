import csv

file = open("Books.csv", "r")
books = list(csv.reader(file))
start_year = int(input("Enter start year: "))
end_year = int(input("Enter end year: "))

for row in books[1:]:
    *_, year = row
    year = int(year)
    if year > start_year and year < end_year:
        print(row)
    

