import turtle
import random

pen = turtle.Turtle()
turtle.colormode(255)
pen.speed(00)

def fill_background():
    penbg = turtle.Turtle()
    penbg.speed(00)
    height = 1200
    width = 1200
    pen.fillcolor('black')
    penbg.begin_fill()
    penbg.goto(-height,-width)
    penbg.goto(-height,width)
    penbg.goto(height,width)
    penbg.goto(height,-width)
    penbg.goto(-height,-width)
    penbg.end_fill()

def pen_position(left_right, up_down):
    pen.up()
    pen.goto(left_right,up_down)
    pen.down()

def draw_zero(red,green,blue,width,amount_angles):
    pen.color(red,green,blue)
    pen.width(width)
    length_line = 1200 / amount_angles
    angle = 360 /amount_angles
    for i in range(amount_angles):
        pen.forward(length_line)
        pen.right(angle)

fill_background()

for i in range (10):
    pen_position(random.randint(-400,0),random.randint(0,300))
    draw_zero(random.randint(0,60), random.randint(50,100), random.randint(150,220),1,3)

pen.hideturtle()

turtle.done()
