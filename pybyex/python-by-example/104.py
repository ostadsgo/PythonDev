people = []
for i in range(4):
    name = input("Enter a name: ")
    age = int(input("Enter a age: "))
    shoe_size = int(input("Shoe size: "))
    row = {"name": name, "age": age, "shoe_size": shoe_size}
    people.append(row)

name = input("Enter name: ")
i = 0
for person in people:
    if person["name"] == name:
        del people[i]
    i += 1

for person in people:
    print(person["name"], person["age"], person["shoe_size"])
