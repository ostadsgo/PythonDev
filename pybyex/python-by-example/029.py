import math


num = int(input("Enter a number bigger than 500 : "))

squared = math.sqrt(num)
result = round(squared, 2)
print("Result with 2 decimal digit is", result)
