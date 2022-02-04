import turtle
import math

turtle.Screen().bgcolor("black")

pen = turtle.Turtle()
pen.pencolor("white")

def letter_v(pen,size):
    v_angle = math.degrees(math.atan(2/8))
    pen.setheading(270)
    pen.left(v_angle)
    v_length_opp = size * 2
    v_length_adj = size * 8
    v_length = math.sqrt((v_length_adj*v_length_adj)+(v_length_opp*v_length_opp))
    pen.forward(v_length)
    pen.setheading(90)
    pen.right(v_angle)
    pen.width(3)
    pen.forward(v_length)

letter_v(pen,10)

turtle.done()
