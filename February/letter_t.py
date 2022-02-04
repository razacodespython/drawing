import turtle

turtle.Screen().bgcolor("black")
pen = turtle.Turtle()
pen.pencolor("white")

def letter_t(pen,size):
    pen.width(3)
    pen.forward(size*1.4)

    pen.width(1)
    pen.right(90)
    pen.forward(size*8)
    pen.back(size*8)

    pen.width(3)
    pen.left(90)
    pen.forward(size*0.6)

    pen.right(90)
    pen.forward(size*8)
    pen.back(size*8)

    pen.left(90)
    pen.forward(size*2)
    pen.hideturtle()
letter_t(pen,10)

turtle.done()
