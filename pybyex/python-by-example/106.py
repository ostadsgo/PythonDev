names = ["John", "Keven", "Bob", "Sam", "Nima"]

file = open("Names.txt", 'w')
for name in names:
    file.write(name + "\n") 
