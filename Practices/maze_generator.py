# TE 2nd Maze Generator
import turtle
import random

def box_setup():
    screen = turtle.Screen()#turtle screen
    screen.setup(2000,1400)
    screen.title("Maze Generator")
    box = turtle.Turtle()
    box.pensize("20")
    box.setpos(0,250)
    box.forward(250)
    
    box.penup()
    box.forward(100)
    box.pendown()
    box.forward(250)
    box.right(90)
    box.forward(600)
    box.right(90)
    box.forward(250)
    
    box.penup()
    box.forward(100)
    box.pendown()
    box.forward(250)
    box.right(90)
    box.forward(350)
box_setup()


maze = turtle.Turtle()
maze.pensize("20")
maze.penup()

maze.setpos(260,250)
maze.pendown()
maze.right(90)
maze.forward(100)
maze.penup()

maze.setpos(350,250)
maze.pendown()
maze.right(90)
maze.right(90)
maze.right(90)
maze.right(90)
maze.forward(100)

rando1 = random.randint(100,600)
maze.penup()
maze.setpos(0,100)
maze.pendown()
maze.right(90)
maze.right(90)
maze.right(90)
maze.forward(rando1)#
maze.penup(600-rando1)

rando2 = random.randint(100,600)
maze.penup()
maze.setpos(0,0)
maze.pendown()
maze.right(90)
maze.right(90)
maze.right(90)
maze.right(90)
maze.forward(rando2)#
maze.penup(600-rando2)#

rando3 = random.randint(100,600)
maze.penup()
maze.setpos(0,-100)
maze.pendown()
maze.right(90)
maze.right(90)
maze.right(90)
maze.right(90)
maze.forward(rando3)#
maze.penup(600-rando3)#

rando4 = random.randint(100,600)
maze.penup()
maze.setpos(0,-200)
maze.pendown()
maze.right(90)
maze.right(90)
maze.right(90)
maze.right(90)
maze.forward(rando4)#
maze.penup(600-rando4)#

#turtle.setpos(0,-20)

turtle.done()