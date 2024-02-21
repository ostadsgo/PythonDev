people = []
for i in range(4):
    name = input("Enter a name: ")
    age = int(input("Enter a age: "))
    shoe_size = int(input("Shoe size: "))
    row = {"name": name, "age": age, "shoe_size": shoe_size}
    people.append(row)

name = input("Enter name: ")

for person in people:
    print(person["name"], person["age"])
