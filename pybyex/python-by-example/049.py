comp_num = 50

guess = int(input("Enter a number: "))
attempt = 1

while guess != comp_num:
    if guess > comp_num:
        guess = int(input("Guess lower: "))
    else:
        guess = int(input("Guess higher: "))

    attempt += 1

print("Well done you took", attempt, "attempts")

