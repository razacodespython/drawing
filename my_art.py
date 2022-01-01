import turtle

pen = turtle.Turtle()

turtle.Screen().bgcolor('black')

turtle.colormode(255)

pen.pencolor('white')

# red = 50, 25, 217, 87, 6
# green = 224, 32, 48, 5, 4
# blue = 250, 168, 255, 230, 212

red = 50
green = 224
blue = 250

pen.pencolor(red,green,blue)

#square
pen.up()
pen.goto(-100,0)
pen.down()
pen.goto(0,100)
pen.goto(100,0)
pen.goto(0,-100)
pen.goto(-100,0)

#outer shapes rectangles
pen.goto(-120,20)
pen.goto(-140,0)
pen.goto(0,-140)
pen.goto(140,0)
pen.goto(120,20)
pen.goto(100,0)

# red = 150, 187, 32, 66, 76
# green = 0, 196, 37, 245, 4
# blue = 190, 57, 179, 75, 112

inner_red = 150
inner_green = 0
inner_blue = 190

pen.pencolor(inner_red,inner_green,inner_blue)
#inner lines
pen.up()
pen.goto(0,-100)
pen.down()

pen.goto(0,0)
pen.goto(50,50)
pen.goto(0,0)
pen.goto(-50,50)

pen.hideturtle()

turtle.done()
