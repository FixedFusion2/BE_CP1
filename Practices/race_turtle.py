# TE 2nd Turtle 

import turtle
import random


#Function for setup
def race_setup():
    screen = turtle.Screen()#turtle screen
    screen.setup(2000,1400)
    screen.title("Turtle Race!")
    finish_line = turtle.Turtle()#finish line setp up variable
    finish_line.penup()#Don't show it moving
    finish_line.setpos(700,0)
    finish_line.right(270)
    finish_line.pendown()
    finish_line.forward(500)#Show the finish line

#Function turtle and race
def race_turtles():
    t1 = turtle.Turtle()#The 5 turtles
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    t4 = turtle.Turtle()
    t5 = turtle.Turtle()
    
    t1.penup()#Don't show tutle setup
    t2.penup()
    t3.penup()
    t4.penup()
    t5.penup()

    t1.setpos(-500,0)#Turt;e setup coordinates
    t2.setpos(-500,100)
    t3.setpos(-500,200)
    t4.setpos(-500,300)
    t5.setpos(-500,400)

    t1.pendown()#Put the pen back
    t2.pendown()
    t3.pendown()
    t4.pendown()
    t5.pendown()

    winner = False#Define winner
    while winner == False:
        turtle_speed_1 = random.randint(1,6)#Set turtle speeds
        turtle_speed_2 = random.randint(1,6)
        turtle_speed_3 = random.randint(1,6)
        turtle_speed_4 = random.randint(1,6)
        turtle_speed_5 = random.randint(1,6)

        turtle_move_1 = random.randint(1,100)#Set turtles moves
        turtle_move_2 = random.randint(1,100)
        turtle_move_3 = random.randint(1,100)
        turtle_move_4 = random.randint(1,100)
        turtle_move_5 = random.randint(1,100)
        
        t1.color("red")#Turtle 1 setup
        t1.shape("turtle")
        t1.speed(turtle_speed_1)
        t1.forward(turtle_move_1)
        if t1.xcor() > 700:#
            font_style = ("Arial", 50, "normal")
            print ("Red Turtle Won")
            winner==True
            t1.write("Red Turtle Won",font = font_style, align ="right")
            break

        t2.color("blue")
        t2.shape("turtle")
        t2.speed(turtle_speed_2)
        t2.forward(turtle_move_2)
        if t2.xcor() > 700:
            font_style = ("Arial", 50, "normal")
            print ("Blue Turtle Won")
            winner==True
            t2.write("Blue Turtle Won",font = font_style, align = "right")
            break

        t3.color("green")
        t3.shape("turtle")
        t3.speed(turtle_speed_3)
        t3.forward(turtle_move_3)
        if t3.xcor() > 700:
            font_style = ("Arial", 50, "normal")
            print ("Green Turtle Won")
            winner==True
            t3.write("Green Turtle Won",font = font_style, align = "right")
            break

        t4.color("purple")
        t4.shape("turtle")
        t4.speed(turtle_speed_4)
        t4.forward(turtle_move_4)
        if t4.xcor() > 700:
            font_style = ("Arial", 50, "normal")
            print ("Purple Turtle Won")
            winner==True
            t4.write("Purple Turtle Won",font = font_style, align = "right")
            break

        t5.color("orange")
        t5.shape("turtle")
        t5.speed(turtle_speed_5)
        t5.forward(turtle_move_5)
        if t5.xcor() > 700:
            font_style = ("Arial", 50, "normal")
            print ("Orange Turtle Won")
            winner==True
            t5.write("Orange Turtle Won",font = font_style, align = "right")
            break

race_setup()
race_turtles()


turtle.done()