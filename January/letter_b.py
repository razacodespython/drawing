import turtle
import math

pen = turtle.Turtle()
turtle.Screen().bgcolor("black")
pen.pencolor("white")
pen.speed(0)


def letter_b(size):
    pen.width(3)
    pen.right(90)
    pen.forward(size*8)  # 80
    pen.width(1)

    pen.setheading(360)
    pen.left(math.degrees(math.atan(1)))
    pen.forward(math.sqrt((size*size)+(size*size)))  # 200

    pen.setheading(360)
    pen.left(90)
    pen.forward(size * 6)  # 60
    pen.setheading(180)
    pen.right(math.degrees(math.atan(1)))
    pen.forward(math.sqrt((size*size)+(size*size)))  # 200

    pen.width(2)
    pen.setheading(360)
    pen.forward(size * 1)  # 10
    pen.right(math.degrees(math.atan(1)))
    pen.forward(math.sqrt((size*size)+(size*size))*2)  # 200

    pen.setheading(180)
    pen.left(math.degrees(math.atan(1)))
    pen.forward(math.sqrt((size*size)+(size*size))*2)  # 200

    pen.setheading(90)
    pen.forward(size * 1)  # 10
    pen.setheading(360)
    pen.right(math.degrees(math.atan(1)))
    pen.forward(math.sqrt((size*size)+(size*size))*3)  # 200

    pen.right(90)
    pen.forward(math.sqrt((size*size)+(size*size))*2)  # 200

    pen.setheading(180)
    pen.forward(size * 2)  # 20
    pen.width(1)
    pen.setheading(360)
    pen.left(math.degrees(math.atan(1)))
    pen.forward(math.sqrt((size*size)+(size*size)))  # 200

    pen.setheading(360)
    pen.forward(size * 2)  # 20


pen.up()
pen.goto(-50, 200)
pen.down()
pen.setheading(360)

pen.hideturtle()


letter_b(40)

turtle.done()
