nums = []

for i in range(3):
    nums.append(int(input("Enter a number: ")))
    print(nums)

while ans := input("Do you want to add more(y/n)? ") == "y":
    nums.append(int(input("Enter a number: ")))
    print(nums)

nums.pop()
print(nums)
