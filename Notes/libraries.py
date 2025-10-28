# TE 2nd Libraries and built in functions
import random
import turtle
number = random.randint(100,500)

turtle.color("#2C0CE6")
turtle.pensize("20")
turtle.fillcolor("green")
turtle.begin_fill()
for x in range(100):
    turtle.speed(25)
    turtle.forward(250)
    turtle.right(100)
turtle.end_fill()

turtle.penup(-50,100)
turtle.goto()

turtle.done()