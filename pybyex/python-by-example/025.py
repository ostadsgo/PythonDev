first_name = input("Enter your first name: ")

if len(first_name) < 5:
    surname = input("Enter your surname: ")
    name = first_name + surname 
    print(name.upper())
else:
    print(first_name.lower())
