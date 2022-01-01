import turtle

pen = turtle.Turtle()

turtle.Screen().bgcolor('black')
pen.pencolor('white')
pen.speed(0)

turtle.colormode(255)

# red = 50, 25, 217, 87
# green = 224, 32, 48, 5
# blue = 250, 168, 255, 230

red = 3
green = 4
blue = 80

pen.pencolor(red,green,blue)
pen.width(7)
#drawing the rectangle
pen.up()
pen.goto(-100,0)
pen.down()
pen.goto(0,100)
pen.goto(100,0)
pen.goto(0,-100)
pen.goto(-100,0)

pen.width(0)
red = 6
green = 4
blue = 212

pen.pencolor(int(red/255),green,blue)

#drawing the rectangle
pen.up()
pen.goto(-100,0)
pen.down()
pen.goto(0,100)
pen.goto(100,0)
pen.goto(0,-100)
pen.goto(-100,0)

#outer space
pen.goto(-120, 20)
pen.goto(-140,0)
pen.goto(0,-140)
pen.goto(140,0)
pen.goto(120,20)
pen.goto(100,0)

# red = 150, 187, 32, 66
# green = 0, 196, 37, 245
# blue = 190, 57, 179, 75

inner_red = 76
inner_green = 4
inner_blue = 112
#inner lines

pen.pencolor(inner_red,inner_green,inner_blue)
pen.up()
pen.goto(0,-100)
pen.down()
pen.goto(0,0)
pen.goto(50,50)
pen.goto(0,0)
pen.goto(-50,50)


pen.hideturtle()
turtle.done()