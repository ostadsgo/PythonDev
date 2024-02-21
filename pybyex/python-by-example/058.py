import random

score = 0
i = 0

while i < 5:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    ans = int(input(f"{num1} + {num2} = "))
    if num1 + num2 == ans:
        score += 1
    i += 1

print("You answerd", score, "questions correctly.")




