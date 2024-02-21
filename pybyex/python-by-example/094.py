from array import *
from random import randrange

nums = []
for _ in range(5):
    nums.append(randrange(1, 100))

print(nums)
n = int(input("Enter a number from the list: "))
try_again = True
while try_again:
    if n in nums:
        print(nums.index(n))
        try_again = False
    else:
        n = int(input("Select a number from the list please: "))





