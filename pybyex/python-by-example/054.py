import random


rand_tail = random.choice(['h', 't'])
response = input("Enter you choice (h/t): ")

if rand_tail == response:
    print("You win.")
else:
    print("Bad luck")
    print("Computer select was,", rand_tail)
