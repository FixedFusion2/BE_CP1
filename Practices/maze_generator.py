# TE 2nd Maze Generator
import turtle


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
    box.forward(500)
    box.right(90)
    box.forward(250)
    box.penup()
    box.forward(100)
    box.pendown()
    box.forward(250)
    box.right(90)
    box.forward(250)
box_setup()

maze = turtle.Turtle()
maze.pensize("20")
maze.penup()
maze.setpos(260,250)
maze.pendown()
maze.right(90)
maze.forward(100)
maze.penup()
maze.setpos(270,250)
maze.pendown()
maze.right(90)
maze.forward(100)


#turtle.setpos(0,-20)

turtle.done()