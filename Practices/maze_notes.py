# TE 2nd Maze Generator
import turtle
import random

def box_setup():
    screen = turtle.Screen()#turtle screen
    screen.setup(2000,1400)
    screen.title("Maze Generator")
    box = turtle.Turtle()
    box.pensize("10")
    
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
rows.pensize(10)
for y in [200, 100, 0, -100, -200]:
    rows.penup()
    rows.setpos(0, y)
    rows.pendown()
    rows.forward(700)

columns = turtle.Turtle()
columns.pensize(10)
columns.right(90)
for x in [100, 200, 300, 400, 500, 600]:
    columns.penup()
    columns.setpos(x, 300)
    columns.pendown()
    columns.forward(600)


path_walls = [
    ((100, 300), "down"),
    ((200, 300), "down"),
    ((300, 300), "down"),
    ((300, 200), "right"),
    ((400, 200), "down"),
    ((400, 100), "right"),
    ((500, 100), "down"),
    ((500, 0), "right"),
]

for x, y in path_walls:
    t = turtle.Turtle()
    t.pensize(10)
    t.penup()
    t.setpos(x, y)
    t.pendown()
    if "right" in path_walls[0][1]:
        t.forward(100)
    else:
        t.right(90)
        t.forward(100)
        t.left(90)


#turtle.setpos(0,-20)

turtle.done()