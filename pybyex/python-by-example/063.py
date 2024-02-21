import turtle

turtle.hideturtle()
turtle.penup()
turtle.backward(150)
turtle.showturtle()
turtle.pendown()
colors = ["red", "green", "blue"]
def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

for c in range(3):
    turtle.color("black", colors[c])
    turtle.begin_fill()
    draw_square()
    turtle.penup()
    turtle.forward(110)
    turtle.pendown()
    turtle.end_fill()


turtle.exitonclick()
