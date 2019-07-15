import turtle
t = turtle.Turtle()
t.hideturtle()
t.penup()
name = "Eric"
message = f"Hello {name}, would you like to learn Python today?"
t.goto(-100, 0)
t.write(message, align="left", font=(20))