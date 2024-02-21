from array import *

nums = array('i', [])
counter = 0

while counter < 5:
    num = int(input("Enter a number: "))
    if num >= 10 and num <= 20:
        nums.append(num)
        counter += 1
    else:
        print("Outside the range.")

print("Thank you.")
for num in nums:
    print(num)
