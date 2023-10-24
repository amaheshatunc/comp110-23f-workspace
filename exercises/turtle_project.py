"""Enjoying the wonders of wordle."""
from turtle import Turtle, colormode, done, setup
import random
from turtle import *
__author__ = "730668496"
colormode(255)
"""This code right here was to make the size window be setup to a certain number of pixels."""
setup(700, 660)
leo: Turtle = Turtle()


def main() -> None:
    """This code is here to run the entire painting. The painting is a beach scene that is under a sunrise which has a coconut on the beach with a ship on the sea."""
    leo.hideturtle()
    leo.speed(200)
    leo.penup()
    leo.goto(-350, -330)
    # Light yellow.
    rectangle(700, 660, 255, 253, 175)
    # Pink.
    rectangle(700, 490, 254, 130, 140)
    # The sun.
    leo.goto(0, -30)
    leo.pendown()
    circle(255, 255, 0, 60)
    leo.penup()
    # Teal.
    leo.goto(-350, -330)
    rectangle(700, 340, 0, 204, 153)
    # The ocean.
    rectangle(700, 220, 79, 66, 181)
    # The beach scene.
    leo.goto(-350,-330)
    leo.pendown()
    rectangle(700, 100, 225, 191, 146)
    leo.goto(-350,-250)
    rectangle(300, 50, 225, 191, 146)
    leo.left(270)
    leo.goto(-50,-200)
    triangle(35, 225, 191, 146)
    # The clouds.
    """The following few lines is displaying how to randomly display clouds across the map."""
    leo.penup()
    leo.goto(random.randint(-120, 190), random.randint(110, 230))
    leo.pendown()
    clouds(30)
    leo.penup()
    leo.goto(random.randint(-120, 190), random.randint(110, 230))
    leo.pendown()
    leo.setheading(130)
    clouds(30)
    # The coconut.
    leo.penup()
    leo.goto(200, -240)
    coconut(200, -250)
    # The ship.
    leo.penup()
    leo.setheading(0)
    trapezoid(-100,-110)
    leo.penup()
    leo.goto(-80,-110)
    leo.setheading(0)
    leo.pendown()
    rectangle(10, 70, 255, 255, 255)
    leo.penup()
    leo.goto(-100,-60)
    leo.pendown()
    triangle(30, 255, 0, 0)
    done()

def rectangle(width: float, height: float, color_one: float, color_two: float, color_three: float) -> None:
    """Rectangle Function."""
    leo.begin_fill()
    leo.color(color_one, color_two, color_three)
    leo.fillcolor(color_one, color_two, color_three)
    i: int = 0
    while (i < 4):
        leo.forward(width)
        leo.left(90)
        leo.forward(height)
        leo.left(90)
        i = i + 1
    leo.end_fill()

def triangle(side: float, color_one: float, color_two: float, color_three: float) -> None:
    """Triangle Function."""
    leo.begin_fill()
    leo.color(color_one, color_two, color_three)
    leo.fillcolor(color_one, color_two, color_three)
    leo.forward(side)
    leo.left(90)
    leo.forward(side)
    leo.left(135)
    leo.forward(side * 1.414)
    leo.end_fill()
    
def circle(color_one: float, color_two: float, color_three: float, radius: float) -> None:
    """Circle Function."""
    leo.begin_fill()
    leo.color(color_one, color_two, color_three)
    leo.fillcolor(color_one, color_two, color_three)
    leo.pencolor(color_one, color_two, color_three)
    leo.circle(radius)
    leo.end_fill()

def clouds(radius: float) -> None:
    """In this function I am trying to make a clouds which can be spawned in anywhere in the world and it can be randomized across the map in a certain area (This can be seen the main function)."""
    leo.begin_fill()
    leo.color(255, 255, 255)
    leo.fillcolor(255, 255, 255)
    leo.pencolor(255, 255, 255)
    i: int = 0
    while (i < 2):
        leo.left(275)
        leo.circle(radius)
        leo.left(85)
        leo.forward(radius + 75)
        leo.left(100)
        leo.circle(radius)
        i = i + 1
    leo.end_fill()

def coconut(x: float, y: float) -> None:
    """In this function I am trying to make a coconuts which can be spawned in anywhere in the world where I call it without using a special formula."""
    leo.goto(x, y)
    leo.pendown()
    circle(101, 67, 33, 20)
    leo.penup()
    leo.goto(x,y + 26)
    leo.pendown()
    circle(0, 0, 0, 3)
    leo.penup()
    leo.goto(x + 6,y + 18)
    leo.pendown()
    circle(0, 0, 0, 3)
    leo.penup()
    leo.goto(x - 6,y + 18)
    leo.pendown()
    circle(0, 0, 0, 3)

def trapezoid(x: float, y: float) -> None: 
    """In this function I am trying to make a trapezoid which can be spawned in anywhere in the world where I call it without using a special formula."""
    leo.goto(x,y)
    leo.pendown()
    rectangle(46, 30, 255, 255, 255)
    leo.setheading(90)
    leo.goto(x, y)
    triangle(30, 255, 255, 255)
    leo.setheading(180)
    leo.goto(x + 77, y + 30)
    triangle(30, 255, 255, 255)


if __name__ == "__main__":
    main()