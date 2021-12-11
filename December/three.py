import turtle

pen = turtle.Turtle()
turtle.colormode(255)
turtle.Screen().bgcolor("black")
pen.color("white")
pen.speed(00)

#first horizontal then vertical

def pen_start(x,y):
    pen.up()
    pen.goto(x,y)
    pen.down()


def draw_square(size):
    pen.forward(size)
    pen.right(90)
    pen.forward(size)
    pen.right(90)
    pen.forward(size)
    pen.right(90)
    pen.forward(size)

pen_start(-100,100)
pen.width(4)
draw_square(200)
pen.width(1)
pen.goto(100,-100)
pen.goto(0,-100)

pen.home()

pen.goto(-100,-100)
pen.goto(-80,-80)

pen.fillcolor("white")
pen.begin_fill()
pen.goto(-80,80)
pen.home()
pen.goto(-80,-80)
pen.goto(-80,80)
pen.end_fill()

pen.up()
pen.goto(25,75)
pen.down()

pen.fillcolor("white")
pen.begin_fill()
draw_square(50)
pen.end_fill()

pen.hideturtle()
turtle.done()



