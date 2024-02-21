from turtle import *
import random

lines = random.randint(5, 20)

for x in range(0, lines):
    length = random.randint(24, 1000)
    rotate = random.randint(1, 356)
    forward(length)
    right(rotate)

exitonclick()
