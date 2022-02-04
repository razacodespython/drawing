import math
import turtle
import letter_f
import letter_e
import letter_a
import letter_r
import time

#dont let fear stop you from achieving greatness. Now go and code some python
pen = turtle.Turtle()
turtle.Screen().bgcolor("black")
pen.pencolor("white")
pen.speed(0)

size = 20

pen.up()
pen.back(size * 10)
pen.down()
pen.hideturtle()
# time.sleep(10)

letter_f.letter_f(pen, size)
pen.setheading(360)
pen.up()
pen.forward(size * 4)
pen.left(90)
pen.forward(size * 8)
pen.setheading(360)
pen.down()
letter_e.letter_e(pen, size)

# pen2.setheading(360)
# pen2.up()
# pen2.forward(size * 1+ size * 4)
# pen.left(90)
# pen.forward(80)
# pen.setheading(360)
# pen.down()

letter_a.letter_a(math, pen, size)

pen.setheading(360)
pen.up()
pen.forward(size * 1)
pen.left(90)
pen.forward(size * 4)
pen.setheading(360)
pen.down()

letter_r.letter_r(math, pen, size)

pen.hideturtle()

turtle.done()
