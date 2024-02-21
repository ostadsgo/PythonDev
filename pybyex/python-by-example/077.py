people = []


for i in range(3):
    name = input("Enter name of the person you want to invite to the party: ")
    people.append(name)

ans = input("Do you want to invite more people(y/n) ? ")
while ans == "y":
    name = input("Enter name of the person you want to invite to the party: ")
    people.append(name)
    ans = input("Do you want to invite more people(y/n) ? ")

print("You invite", len(people), "people.")
print(people)

person = input("Enter name of a person from list: ")
print("Index of", person, "is", people.index(person))
ans = input("Would you like to invite that person to the party(y/n)? ")
if ans == "n":
    people.remove(person)

print(people)
