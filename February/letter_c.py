import turtle

turtle.Screen().bgcolor("black")
pen = turtle.Turtle()
pen.pencolor("white")

def letter_c(pen,size):
    pen.width(3)
    pen.forward(size*4)
    pen.back(size*4)
    pen.right(90)
    pen.forward(size*8)
    pen.left(90)
    pen.forward(size*4)
    pen.back(size*3)

    pen.width(1)
    pen.left(90)
    pen.forward(size*8)

    pen.hideturtle()

letter_c(pen,10)

turtle.done()