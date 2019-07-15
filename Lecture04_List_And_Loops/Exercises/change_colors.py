import turtle    # importing the module
import random    # importing random module for generating random numbers
t = turtle.Turtle()    #making a turtle object of Turtle class for drawing
screen=turtle.Screen()    #making a canvas for drawing
screen.setup(420,320)    #choosing the screen size
screen.bgcolor('black')    #making canvas black
t.pensize(4)    #choosing the size of pen nib
t.speed(1)    #choosing the speed of drawing
t.shape('turtle')   #choosing the shape of pen nib
n=0
while n<7:
    r=random.randint(1,120)   #random numbers for red
    g=random.randint(81,200)   #random numbers for green
    b=random.randint(61,255)   #random numbers for blue
    turtle.colormode(255)   #declaring the colour mode
    t.pencolor(r,g,b)   #pen colour
    n=n+1
    t.penup()
    t.setpos(0,-n*20)
    t.pendown()
    t.circle(20*n)
