row6.penup()
row6.setpos(0,-250)
while row5.xcor() < 700:
    rand=random.randint(1,2)
    if rand == 1:
        row6.penup()
        row6.forward(100)
    else:
        row6.pendown()
        row6.forward(100)

row7.penup()
row7.setpos(0,-350)
while row5.xcor() < 700:
    rand=random.randint(1,2)
    if rand == 1:
        row7.penup()
        row7.forward(100)
    else:
        row7.pendown()
        row7.forward(100)