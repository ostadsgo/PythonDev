direction = input("Which direction would like to count (up/down)? ")
direction = direction.lower()

if direction == "up":
    number = int(input("Enter a number: "))
    for i in range(1, number+1):
        print(i)

elif direction == "down":
    number = int(input("Enter a number: "))
    for i in range(20, number-1, -1):
        print(i)
else:
    print("I don't understand.")
