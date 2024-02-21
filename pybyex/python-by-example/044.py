number = int(input("How many pepole do want to invite? "))

if number > 10:
    print("Too many people.")
else:
    for i in range(number):
        guest_name = input("Enter guest name: ")
        print(guest_name, "invited.")
