import csv


def add_to_file():
    file = open("a.csv", "a")
    name = input("Enter a name: ")
    row = (name,)
    csv_writer = csv.writer(file)
    csv_writer.writerow(row)
    file.close()

def view_records():
    file = open("a.csv", "r")
    csv_reader = csv.reader(file)
    rows = list(csv_reader)
    index_row = 0
    for row in rows:
        print(index_row, row)
        index_row += 1

def delete_record():
    view_records()
    index = int(input("Enter index of the row to delete: "))
    reader = csv.reader(open("a.csv", "r"))
    rows = list(reader)
    del rows[index]
    # write again
    file = open("a.csv", "w")
    csv_writer = csv.writer(file)
    for row in rows:
        csv_writer.writerow(row)
    file.close()

def main():
    menu = (
        "1) Add to file\n"
        "2) View all records\n"
        "3) Delete a record\n"
        "4) Quit program\n"
        "Enter the number of your selection: "
    )
    running = True
    while running:
        response = input(menu)
        if response == "1":
            add_to_file()
        elif response == "2":
            view_records()
        elif response == "3":
            delete_record()
        elif response == "4":
            running = False
        else:
            print("Choosing wrong option.")

main()
