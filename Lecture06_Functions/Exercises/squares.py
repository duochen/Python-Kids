import turtle

def square(t, side):
    for i in range(4):
        t.forward(side)
        t.left(90)

t = turtle.Turtle()
t.hideturtle()

square(t, 100)

t.penup()
t.left(90)
t.forward(200)
t.pendown()
square(t, 100)




