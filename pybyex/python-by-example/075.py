nums = [321, 432, 433, 932, 111]

for num in nums:
    print(num)

n = int(input("Enter a number from list: "))

if n in nums:
    print(nums.index(n))
else:
    print("The number is not in the list.")
