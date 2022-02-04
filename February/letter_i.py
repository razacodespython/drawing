import turtle

turtle.Screen().bgcolor("black")
pen = turtle.Turtle()
pen.pencolor("white")

def letter_i(pen,size):
    pen.width(3)
    pen.forward(size*4)
    pen.back(size*4)

    pen.width(1)

    pen.up()
    pen.forward(size*1.5)
    pen.down()
    pen.right(90)
    pen.forward(size*8)
    pen.back(size*8)

    pen.width(3)
    pen.up()
    pen.left(90)
    pen.forward(size*0.5)
    pen.down()
    pen.right(90)
    pen.forward(size*8)

    pen.left(90)
    pen.forward(size*2)
    pen.back(size*4)

    pen.hideturtle()

letter_i(pen,10)

turtle.done()