# import turtle
# import math

# turtle.Screen().bgcolor("black")
# pen = turtle.Turtle()
# pen.pencolor("white")


def letter_r(math, pen, size):
    pen.width(3)
    pen.right(90)
    pen.forward(size*8)  # 80
    pen.width(1)

    pen.up()
    pen.setheading(360)
    pen.forward(size*1)
    # pen.left(math.degrees(math.atan(1)))
    # pen.forward(math.sqrt((size*size)+(size*size)))  # 200
    pen.down()

    pen.setheading(360)
    pen.left(90)
    pen.forward(size * 7)  # 60
    pen.setheading(180)
    pen.up()
    pen.right(math.degrees(math.atan(1)))
    pen.forward(math.sqrt((size*size)+(size*size)))  # 200
    pen.down()

    pen.width(3)
    pen.setheading(360)
    pen.forward(size * 2)  # 10
    pen.right(math.degrees(math.atan(1)))
    pen.forward(math.sqrt((size*size)+(size*size))*2)  # 200

    pen.setheading(180)
    pen.left(math.degrees(math.atan(1)))
    pen.forward(math.sqrt((size*size)+(size*size))*2)  # 200

    pen.setheading(90)
    pen.forward(size * 1)  # 10
    pen.setheading(360)
    pen.right(math.degrees(math.atan(1)))
    pen.forward(math.sqrt((size*size)+(size*size))*2)  # 200

    pen.setheading(360)
    pen.right(90)
    pen.forward(size*3)


# letter_r(20)

# turtle.done()
