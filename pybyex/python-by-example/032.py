import math


radius = int(input("Enter radius: "))
depth = int(input("Enter depth of cylinder: "))

area = math.pi * radius ** 2
volume = area * depth

print("Total volume is", volume)
