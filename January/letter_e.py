# import turtle
# import math

# pen_now = turtle.Turtle()
# pen_now.pencolor("white")
# turtle.Screen().bgcolor("black")


def letter_e(pen, size):
    pen.width(3)
    pen.forward(size * 4)  # 40
    pen.back(size * 4)  # 40

    pen.right(90)
    pen.forward(size * 3)  # 30

    pen.width(1)
    pen.left(90)
    pen.forward(size * 3)  # 30
    pen.back(size * 3)  # 30

    pen.width(3)
    pen.right(90)
    pen.forward(size * 1)  # 10

    pen.width(3)
    pen.left(90)
    pen.forward(size * 3)  # 30
    pen.back(size * 3)  # 30

    pen.right(90)
    pen.forward(size * 4)  # 40

    pen.left(90)
    pen.forward(size * 1)  # 10

    pen.width(1)
    pen.left(90)
    pen.forward(size * 7)  # 70
    pen.back(size * 7)  # 70

    pen.width(3)
    pen.right(90)
    pen.forward(size * 3)  # 30


# letter_e(pen_now, 30)

# turtle.done()
