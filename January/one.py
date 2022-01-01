import turtle

pen = turtle.Turtle()
turtle.Screen().bgcolor('black')
pen.pencolor('white')
turtle.colormode(255)
pen.speed(0)

pen.up()
pen.goto(-100,-50)
pen.down()

#glow
red_g = 0 #0,0,21
green_g = 80 #60, 40,20,0
blue_g = 43

pen.pencolor(red_g,green_g,blue_g)
pen.width(7)

for i in range(6):
   pen.forward(40)
   pen.left(120+180)
   pen.forward(80)
   for j in range(6):
       pen.forward(20)
       pen.setheading(60+i*60)
   pen.backward(80)
   pen.setheading(60+i*60)
   #pen.write(str(pen.pos()))

#inner line
red = 0 #0,0,117
green = 230 #180,140,110,0
blue = 140  #202,242,242,242


pen.pencolor(red,green, blue)
pen.width(1)

for i in range(6):
   pen.forward(40)
   pen.left(120+180)
   pen.forward(80)
   for j in range(6):
       pen.forward(20)
       pen.setheading(60+i*60)
   pen.backward(80)
   pen.setheading(60+i*60)

pen.hideturtle()
turtle.done()

#example set heading and angles
# pen.forward(100)
# pen.setheading(90)
# pen.forward(100)
# pen.setheading(180)
# pen.forward(100)
# pen.setheading(270)
# pen.forward(100)
