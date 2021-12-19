import turtle

#initialize turtle
pen = turtle.Turtle()
pen.speed(00)

#define background color
turtle.Screen().bgcolor('black')

#define color
turtle.colormode(255)

red = 50     #117
green = 224
blue = 230

pen.pencolor(red,green,blue)

for i in range(25):
    pen.left(90-i)
    pen.forward(200)
    pen.right(90)
    pen.forward(200)
    pen.right(90)
    pen.forward(320)
    pen.home()

#hides the pen
pen.hideturtle()

#keeps the window open after turtle is done
turtle.done()