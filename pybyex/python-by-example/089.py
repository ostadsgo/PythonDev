from array import *
from random import randrange

nums = array('i', [1, 2, 3, 4, 5])

for _ in range(5):
    nums.append(randrange(1, 100))

for num in nums:
    print(num)
