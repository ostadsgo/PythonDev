import random 


num = random.randint(1, 5)
guess = int(input("I am number between 1 and 5, guess me: "))
if num == guess:
    print("Well done.")
else:
    print('here', num)
    if guess < num:
        guess = int(input("Guess high: "))
        if guess == num:
            print("Well done.")
        else:
            print("You lose.")
    else:
        guess = int(input("Geuss low: "))
        if guess == num:
            print("Well done.")
        else:
            print("You lose.")


