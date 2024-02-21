menu = """
1) Create a new file
2) Display the file
3) Add a new item to the file
Make a selection 1, 2, or 3
> """

response = input(menu)
if response == "1":
    file = open("Subject.txt", "w")
    subject = input("Enter a school subject: ")
    file.write(subject + "\n")
    file.close()
elif response == "2":
    file = open("Subject.txt", "r")
    print(file.read())
elif response == "3":
    file = open("Subject.txt", "a")
    subject = input("Enter a school subject: ")
    file.write(subject + "\n")
    file.close()
    file = open("Subject.txt", "r")
    print(file.read())
else:
    print("Error! Invlid choice.")

    

