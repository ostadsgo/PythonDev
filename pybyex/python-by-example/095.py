from array import *
from random import randrange

nums = array('d', [randrange(10, 100) / 10 for num in range(5)])

n = int(input("Enter a number between 2 and 5 : "))

again = True
while again: 
    if n >= 2 and n <= 5:
        for num in nums:
            print(round(num / n, 2))
        again = False
    else:
        n = int(input("Please enter number between 2 and 5 : "))

