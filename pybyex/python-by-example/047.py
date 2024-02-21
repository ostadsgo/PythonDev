num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

total = num1 + num2

ans = input("Do you want to add another number[y/n]: ")

while ans.lower() == 'y':
    num = int(input("Enter a number: "))
    total += num
    ans = input("Do you want to add another number[y/n]: ")

print("The total is", total)
