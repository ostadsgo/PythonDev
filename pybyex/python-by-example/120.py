import random


def add():
    x = random.randrange(5, 20)
    y = random.randrange(5, 20)
    correct = x + y
    ans = int(input(f"{x} + {y} = "))
    return ans, correct

def subtraction():
    x = random.randrange(25, 50)
    y = random.randrange(1, 25)
    correct = x - y
    ans = int(input(f"{x} - {y} = "))
    return ans, correct

def check_ans(correct, ans):
    if correct == ans:
        return "Correct"
    return f"Incorrect the answer is, {correct}"

def main():
    menu = "1) Addition\n2) Subtraction\nEnter 1 or 2: "
    response = input(menu)
    if response == "1":
        ans, correct = add()
        res = check_ans(correct, ans)
    elif response == "2":
        ans, correct = add()
        res = check_ans(correct, ans)
    else:
        res = "Incorrect choice."

    print(res)


main()
