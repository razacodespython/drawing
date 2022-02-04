import turtle
import math

turtle.Screen().bgcolor("black")
pen = turtle.Turtle()
pen.pencolor("white")

def letter_d(pen,size):
    pen.width(3)
    pen.forward(size*3)
    pen.right(math.degrees(math.atan(1)))
    pen.forward(math.sqrt((size*size)+(size*size)))

    pen.setheading(270)
    pen.forward(size*6)
    pen.right(math.degrees(math.atan(1)))
    pen.forward(math.sqrt((size*size)+(size*size)))

    pen.setheading(180)
    pen.forward(size*2)

    pen.width(1)
    pen.right(90)
    pen.forward(size*8)
    pen.back(size*8)

    pen.width(3)
    pen.left(90)
    pen.forward(size*1)

    pen.right(90)
    pen.forward(size*8)

    pen.hideturtle()

letter_d(pen,10)

turtle.done()