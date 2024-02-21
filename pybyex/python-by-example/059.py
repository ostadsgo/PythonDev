import random


color = random.choice(["red", "green", "blue", "black", "white"])

guess = input("I am a random color name guess me: ")

while guess != color:
    guess = input(f"No color look like {color.upper()}: ")
print("Well done.")
