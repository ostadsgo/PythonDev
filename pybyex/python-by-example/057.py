import random


num = random.randint(1, 10)

guess = int(input("Enter a number: "))

while guess != num:
    if guess < num:
        guess = int(input("Enter higher number: "))
    else:
        guess = int(input("Enter lower number: "))
