# TE 2nd Maze Generator

import turtle
import random


#Set variables and functions
def box_setup():
    screen = turtle.Screen()#turtle screen
    screen.setup(2000,1400)
    screen.title("Maze Generator")
    box = turtle.Turtle()
    box.pensize("10")
    
    box.setpos(0,350)#The box
    box.forward(300)
    box.penup()
    box.forward(100)
    box.pendown()
    box.forward(300)
    box.right(90)
    box.forward(700)
    box.right(90)
    box.forward(300)
    box.penup()
    box.forward(100)
    box.pendown()
    box.forward(300)
    box.right(90)
    box.forward(350)


box_setup()

row1 = turtle.Turtle()
row1.pensize("10")
row2 = turtle.Turtle()
row2.pensize("10")
row3 = turtle.Turtle()
row3.pensize("10")
row4 = turtle.Turtle()
row4.pensize("10")
row5 = turtle.Turtle()
row5.pensize("10")
row6 = turtle.Turtle()
row6.pensize("10")

row1.penup()
row1.setpos(0,250)
while row1.xcor() < 700:
    rand=random.randint(1,2)
    if rand == 1:
        row1.penup()
        row1.forward(100)
    else:
        row1.pendown()
        row1.forward(100)


row2.penup()
row2.setpos(0,150)
while row2.xcor() < 700:
    rand=random.randint(1,2)
    if rand == 1:
        row2.penup()
        row2.forward(100)
    else:
        row2.pendown()
        row2.forward(100)

row3.penup()
row3.setpos(0,50)
while row3.xcor() < 700:
    rand=random.randint(1,2)
    if rand == 1:
        row3.penup()
        row3.forward(100)
    else:
        row3.pendown()
        row3.forward(100)

row4.penup()
row4.setpos(0,-50)
while row4.xcor() < 700:
    rand=random.randint(1,2)
    if rand == 1:
        row4.penup()
        row4.forward(100)
    else:
        row4.pendown()
        row4.forward(100)

row5.penup()
row5.setpos(0,-150)
while row5.xcor() < 700:
    rand=random.randint(1,2)
    if rand == 1:
        row5.penup()
        row5.forward(100)
    else:
        row5.pendown()
        row5.forward(100)

row6.penup()
row6.setpos(0,-250)
while row6.xcor() < 700:
    rand=random.randint(1,2)
    if rand == 1:
        row6.penup()
        row6.forward(100)
    else:
        row6.pendown()
        row6.forward(100)




column1 = turtle.Turtle()
column1.pensize("10")

column1.penup()
column1.setpos(100,350)
column1.right(90)
while column1.ycor() < 700:
    rand=random.randint(1,2)
    if rand == 1:
        column1.penup()
        column1.forward(100)
    else:
        column1.pendown()
        column1.forward(100)

turtle.done()