file = open("Names.txt", "r")
print(file.read())

name = input("Enter a name to remove: ")
file = open("Names.txt", "r")
file2 = open("Names2.txt", "w")
for row in file:
    if name + "\n" != row:
        file2.write(row)
file2.close()
file.close()

file = open("Names2.txt", "r")
print(file.read())
file.close()

