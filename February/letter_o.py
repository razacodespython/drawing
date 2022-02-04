import turtle
import math

turtle.Screen().bgcolor("black")
pen = turtle.Turtle()
pen.pencolor("white")

def letter_o(pen,size):
    pen.width(3)
    pen.right(90)
    pen.forward(size*8)

    pen.left(90)
    pen.forward(size *1)

    pen.width(1)
    pen.left(90)
    pen.forward(size*8)
    pen.back(size*8)

    pen.width(3)
    pen.right(90)
    pen.forward(size*3)

    pen.left(90)
    pen.forward(size*8)
    
    pen.left(90)
    pen.forward(size*4)

    pen.hideturtle()

letter_o(pen, 10)

turtle.done()