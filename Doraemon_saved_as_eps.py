from turtle import *
from math import *

import turtle

turtle.ht()
turtle.speed(0)

def move():
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()
 
turtle.fillcolor("blue")
turtle.begin_fill()
#face1
x = 60
y = 0
move()
turtle.left(60)
turtle.circle(40 * sqrt(3), 240)
turtle.left(60)
turtle.forward(120)
turtle.end_fill()

turtle.fillcolor("white") #different from replit
turtle.begin_fill() #different from replit
#face2
x = 50
y = 0
move()
turtle.left(60)
turtle.circle(100 / sqrt(3), 75)
turtle.right(45)
turtle.circle(20, 180)
turtle.right(180)
turtle.circle(20, 180)
turtle.right(45)
turtle.circle(100 / sqrt(3), 75)
turtle.end_fill() #different from replit

#eyes
x = 0
y = (50 / sqrt(3)) + (100 / sqrt(6))
move()
turtle.right(30)
turtle.circle(20, 360)
turtle.right(180)
turtle.circle(20, 360)

#eyeballs
x = 9
y = (50 / sqrt(3)) + (100 / sqrt(6))
move()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(3, 360)
turtle.right(180)
x = -38
y = (50 / sqrt(3)) + (100 / sqrt(6))
move()
turtle.circle(3, 360)
turtle.right(180)
turtle.end_fill()

#nose and mouth
turtle.fillcolor("red")
turtle.begin_fill()
x = 5
y = 54
move()
turtle.circle(5, 360)
turtle.right(180)
turtle.end_fill()

x = 0
y = 49
move()
turtle.forward(30)
x = -30
y = 10
move()
turtle.left(105)
turtle.forward(32)
turtle.right(30)
turtle.forward(32)

#whisker
z = 50
x = 15
y = 25
move()
turtle.left(15)
turtle.forward(z)
x = 15
y = 28
move()
turtle.left(15)
turtle.forward(z)
x = 15
y = 31
move()
turtle.left(15)
turtle.forward(z)

x = -15
y = 31
move()
turtle.left(120)
turtle.forward(z)
x = -15
y = 28
move()
turtle.left(15)
turtle.forward(z)
x = -15
y = 25
move()
turtle.left(15)
turtle.forward(z)

ts = turtle.getscreen()
ts.getcanvas().postscript(file="duck.eps")
