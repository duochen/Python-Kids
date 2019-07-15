import turtle
t = turtle.Turtle()
t.hideturtle()
t.penup()
quote = "A person who never made a mistake never tried anything new."
author = "Albert Einstein"
t.goto(-100, 0)
t.write(f'{author} once said "{quote}"')
