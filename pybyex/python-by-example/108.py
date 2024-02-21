name = input("Enter a name: ")

f = open("Names.txt", 'a')
f.write(name + '\n')

f.close()

f = open("Names.txt", 'r')
print(f.read())
