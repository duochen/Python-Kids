import turtle
size=None
shape=input("What do you want me to draw? ")
if shape=="square":
    size=input("Please enter the size of a side:")
    size=int(size)
    t=turtle.Pen()
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.hideturtle()
elif shape=="circle":
    size=input("Please enter the radius of the circle:")
    size=int(size)
    t=turtle.Pen()
    t.circle(size)
    t.hideturtle()
else:
    print("Wrong input. You can only enter circle or square")
