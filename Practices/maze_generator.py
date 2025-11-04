# TE 2nd Maze Generator
import turtle
import random

def box_setup():
    screen = turtle.Screen()#turtle screen
    screen.setup(2000,1400)
    screen.title("Maze Generator")
    box = turtle.Turtle()
    box.pensize("10")
    box.speed(100)
    
    box.setpos(0,300)
    box.forward(300)
    box.penup()
    box.forward(100)
    box.pendown()
    box.forward(300)
    box.right(90)
    box.forward(600)
    box.right(90)
    box.forward(300)
    
    box.penup()
    box.forward(100)
    box.pendown()
    box.forward(300)
    box.right(90)
    box.forward(300)
box_setup()


rows = turtle.Turtle()
rows.pensize("10")
rows.speed(100)
rows.penup()
rows.setpos(0,200)
rows.pendown()
rows.forward(700)

rows.penup()
rows.setpos(0,100)
rows.pendown()
rows.forward(700)

rows.penup()
rows.setpos(0,0)
rows.pendown()
rows.forward(700)

rows.penup()
rows.setpos(0,-100)
rows.pendown()
rows.forward(700)

rows.penup()
rows.setpos(0,-200)
rows.pendown()
rows.forward(700)



columns = turtle.Turtle()
columns.pensize("10")
columns.speed(100)
columns.penup()
columns.setpos(100,300)
columns.pendown()
columns.right(90)
columns.forward(600)

columns.penup()
columns.setpos(200,300)
columns.pendown()
columns.forward(600)

columns.penup()
columns.setpos(300,300)
columns.pendown()
columns.forward(600)

columns.penup()
columns.setpos(400,300)
columns.pendown()
columns.forward(600)

columns.penup()
columns.setpos(500,300)
columns.pendown()
columns.forward(600)

columns.penup()
columns.setpos(600,300)
columns.pendown()
columns.forward(600)


#turtle.setpos(0,-20)

turtle.done()