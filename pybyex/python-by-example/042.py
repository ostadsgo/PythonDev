total = 0

for i in range(5):
    number = int(input("Enter a number: "))
    response = input("Would you like to add it to total (y/n)? ")
    if response.lower() == 'y':
        total += number

print("The total is", total)
