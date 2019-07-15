import turtle
t = turtle.Turtle()
t.hideturtle()
t.penup()
name = "Albert Einstein"
t.write(name.upper(), font=(20))
t.goto(0, -50)
t.write(name.lower(), font=(20))
t.goto(0, -100)
name = "albert einstein"
t.write(name.title(), font=(20))
