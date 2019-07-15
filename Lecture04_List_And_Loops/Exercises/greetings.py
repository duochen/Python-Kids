import turtle
t = turtle.Turtle()
t.hideturtle()
t.penup()
names = ["Donald Trump", "Steve Jobs", "Bill Gates", "Warren Buffet"]
message = " loves Python"
t.write(names[0] + message, font=(20))
t.left(90)
t.forward(50)
t.write(names[1] + message, font=(20))
t.forward(50)
t.write(names[2] + message, font=(20))
t.forward(50)
t.write(names[3] + message, font=(50))