from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
bob: Turtle = Turtle()

leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)

# How to make a square. 
i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i = i + 1

# How to make a triangle. 
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

# How to do GoTo, Penup and Pendown
leo.penup()
leo.goto(45, 60)
leo.pendown()

i: int = 0
while (i < 3):
    leo.begin_fill()
    leo.color(99, 204, 250)
    leo.color("blue")
    leo.fillcolor(32, 67, 93)
    leo.speed(50)
    leo.hideturtle()
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()
    
    
bob.color("black")
bob.penup()
bob.goto(0, 0)
bob.pendown()
bob.speed(60)

side_length: int = 300
i: int = 0
while (i < 6):
    bob.forward(side_length)
    bob.left(122)
    i = i + 1
    side_length = side_length * 0.97


leo.begin_fill()
leo.fillcolor(0,255,0)
i = 0
leo.speed(50)
leo.hideturtle()

while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i += 1
leo.end_fill()


done()