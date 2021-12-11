import turtle
from tkinter import *

pen = turtle.Turtle()
turtle.colormode(255)
pen.speed(000)

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


def draw_art():
    for i in range(25):
        red = 3
        blue = 230
        green = 124
        pen.pencolor(red,green,blue)
        pen.left(125+i*2)
        pen.forward(400)
        pen.right(90)
        pen.forward(200)
        pen.right(155)
        pen.forward(280)
        pen.home()
    

screen = turtle.Screen()
fill_background()
draw_art()



pen.hideturtle()

screen_h = 1200
screen_w = 1200

ts = pen.getscreen()
ts.setup(screen_h,screen_w)

canvas = ts.getcanvas()

#canvas.postscript(file="gen_8.eps")
screen.exitonclick()

#turtle.done()