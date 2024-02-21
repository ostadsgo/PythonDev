import csv


def add_to_file():
    file = open("Salaries.csv", "a")
    name = input("Enter a name: ")
    csv_writer = csv.writer(file)
    csv_writer.writerow((name,))
    file.close()

def view_records():
    csv_reader = csv.reader(open("Salaries.csv", "r"))
    for name, salary in csv_reader:
        print(name, salary)

def main():
    menu = (
        "1) Add to file\n"
        "2) View all records\n"
        "3) Quit program\n"
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
            running = False
        else:
            print("Choosing wrong option.")
main()
