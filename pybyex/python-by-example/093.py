from array import *


nums = array('i', [])
for i in range(5):
    nums.append(int(input("Enter a number: ")))

print(nums)

new_arr = array('i', [])
n = int(input("Enter a number to delete: "))
nums.remove(n)
new_arr.append(n)

print(nums)

