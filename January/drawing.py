import turtle

pen = turtle.Turtle()
turtle.Screen().bgcolor('black')
pen.pencolor('white')
pen.speed(0)

turtle.colormode(255)

pen.up()
pen.goto(-100,-50)
pen.down()

glow_red = 21
glow_green = 0
glow_blue = 43

pen.width(9)
pen.pencolor(glow_blue,glow_green,glow_red)

loops = 6

for i in range(loops):
    pen.forward(40)
    pen.left(120+180)
    pen.forward(80)
    for j in range(loops):
        pen.forward(20)
        pen.setheading(60+i*60)
    pen.backward(80)
    pen.setheading(60+i*60)

red = 117
green = 0
blue = 242

pen.width(1)
pen.pencolor(blue,green,red)

loops = 6

for i in range(loops):
    pen.forward(40)
    pen.left(120+180)
    pen.forward(80)
    for j in range(loops):
        pen.forward(20)
        pen.setheading(60+i*60)
    pen.backward(80)
    pen.setheading(60+i*60)

pen.hideturtle()
turtle.done()