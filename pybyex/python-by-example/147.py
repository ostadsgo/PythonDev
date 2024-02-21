import random


colors = ["r", "g", "b", "y", "w", "b"]
colors = random.choices(colors, k=4)
print(colors)

guess_number = 0
while True:
    response = input("Guesses sep by comma: ").strip().split(',')  

    for color, guess, in zip(colors, response): 
        if color == guess:
            print("Correct index and correct color;")
        elif guess in colors and response.count(guess) <= colors.count(guess):
            print("Correct color but wrong place")
        else:
            print("Wrong color.")

    guess_number += 1
    if colors == response:
        break

print(f"You've guessed it in {guess_number} times.")
