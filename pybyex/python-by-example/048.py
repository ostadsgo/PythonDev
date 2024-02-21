ans = 'y'
people_count = 0

while ans.lower() == 'y':
    name = input("Enter name of the guest: ")
    print(name.title(), "has now been invited.")
    ans = input("Would you like to invite more [y/n]: ")
    people_count += 1

print(people_count, "people have been invited.")
