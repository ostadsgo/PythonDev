from turtle import *
import random


pensize(3)

for i in range(0, 8):
    color(random.choice(["red", "green", "blue"]))
    forward(50)
    right(45)

exitonclick()
