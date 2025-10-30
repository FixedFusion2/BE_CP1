# TE 2nd Turtle 

import turtle
import random

def race_setup():
    screen = turtle.Screen()
    screen.setup(1500,1000)
    screen.title("Turtle Race!")
    finish_line = turtle.Turtle()
    finish_line.setpos(500,0)
    finish_line.right(270)
    finish_line.forward(500)

def race_turtles():
    turtle_speed_1 = random.randint(1,6)
    turtle_speed_2 = random.randint(1,6)
    turtle_speed_3 = random.randint(1,6)
    turtle_speed_4 = random.randint(1,6)
    turtle_speed_5 = random.randint(1,6)
    
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    t4 = turtle.Turtle()
    t5 = turtle.Turtle()

    t1.color("red")
    t1.shape("turtle")
    t1.speed(turtle_speed_1)
    t1.forward(500)

    t2.setpos(0,100)
    t2.color("blue")
    t2.shape("turtle")
    t2.speed(turtle_speed_2)
    t2.forward(500)

    t3.color("green")
    t3.shape("turtle")
    t3.setpos(0,200)
    t3.speed(turtle_speed_3)
    t3.forward(500)

    t4.color("purple")
    t4.shape("turtle")
    t4.setpos(0,300)
    t4.speed(turtle_speed_4)
    t4.forward(500)

    t5.color("orange")
    t5.shape("turtle")
    t5.setpos(0,400)
    t5.speed(turtle_speed_5)
    t5.forward(500)

race_setup()
race_turtles()


turtle.done()