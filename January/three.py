import turtle
import math

from numpy import mat

pen = turtle.Turtle()
pen.speed(0)
pen.right(90)
pen.forward(80)

pen.setheading(360)
pen.left(math.degrees(math.atan(1)))
pen.forward(math.sqrt(200))

pen.setheading(360)
pen.left(90)
pen.forward(60)
pen.setheading(180)
pen.right(math.degrees(math.atan(1)))
pen.forward(math.sqrt(200))

pen.setheading(360)
pen.forward(10)
pen.right(math.degrees(math.atan(1)))
pen.forward(math.sqrt(200)*2)

pen.setheading(180)
pen.left(math.degrees(math.atan(1)))
pen.forward(math.sqrt(200)*2)

pen.setheading(90)
pen.forward(10)
pen.setheading(360)
pen.right(math.degrees(math.atan(1)))
pen.forward(math.sqrt(200)*3)

pen.right(90)
pen.forward(math.sqrt(200)*2)

pen.setheading(180)
pen.forward(20)

pen.setheading(360)
pen.left(math.degrees(math.atan(1)))
pen.forward(math.sqrt(200))

pen.setheading(360)
pen.forward(20)

pen.hideturtle()


turtle.done()
