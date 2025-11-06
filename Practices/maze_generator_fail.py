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
    box.speed(0)

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
row1.speed(0)
row2 = turtle.Turtle()
row2.pensize("10")
row2.speed(0)
row3 = turtle.Turtle()
row3.pensize("10")
row3.speed(0)
row4 = turtle.Turtle()
row4.pensize("10")
row4.speed(0)
row5 = turtle.Turtle()
row5.pensize("10")
row5.speed(0)
row6 = turtle.Turtle()
row6.pensize("10")
row6.speed(0)

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
column1.speed(0)
column2 = turtle.Turtle()
column2.pensize("10")
column2.speed(0)
column3 = turtle.Turtle()
column3.pensize("10")
column3.speed(0)
column4 = turtle.Turtle()
column4.pensize("10")
column4.speed(0)
column5 = turtle.Turtle()
column5.pensize("10")
column5.speed(0)
column6 = turtle.Turtle()
column6.pensize("10")
column6.speed(0)


column1.penup()
column1.setpos(100,350)
column1.right(90)
while column1.ycor() > -350:
    rand=random.randint(1,2)
    if rand == 1:
        column1.penup()
        column1.forward(100)
    else:
        column1.pendown()
        column1.forward(100)

column2.penup()
column2.setpos(200,350)
column2.right(90)
while column2.ycor() > -350:
    rand=random.randint(1,2)
    if rand == 1:
        column2.penup()
        column2.forward(100)
    else:
        column2.pendown()
        column2.forward(100)

column3.penup()
column3.setpos(300,350)
column3.right(90)
while column3.ycor() > -350:
    rand=random.randint(1,2)
    if rand == 1:
        column3.penup()
        column3.forward(100)
    else:
        column3.pendown()
        column3.forward(100)

column4.penup()
column4.setpos(400,350)
column4.right(90)
while column4.ycor() > -350:
    rand=random.randint(1,2)
    if rand == 1:
        column4.penup()
        column4.forward(100)
    else:
        column4.pendown()
        column4.forward(100)

column5.penup()
column5.setpos(500,350)
column5.right(90)
while column5.ycor() > -350:
    rand=random.randint(1,2)
    if rand == 1:
        column5.penup()
        column5.forward(100)
    else:
        column5.pendown()
        column5.forward(100)

column6.penup()
column6.setpos(600,350)
column6.right(90)
while column6.ycor() > -350:
    rand=random.randint(1,2)
    if rand == 1:
        column6.penup()
        column6.forward(100)
    else:
        column6.pendown()
        column6.forward(100)        
turtle.done()