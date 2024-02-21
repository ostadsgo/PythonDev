import random


num = random.randint(1, 10)

response = int(input("Enter a number: "))

while response != num:
    response = int(input("Enter new number: "))

