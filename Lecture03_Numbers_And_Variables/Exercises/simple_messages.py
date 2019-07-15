import turtle
t = turtle.Turtle()
t.hideturtle()  # hide turtle
t.penup()       # don't draw line         
t.pencolor('green')
message = 'Hello Python'
t.write(message, font=(20))
t.left(90)
t.forward(50)
t.pencolor('blue')
message = 'I love Python'
t.write(message, font=(20))
