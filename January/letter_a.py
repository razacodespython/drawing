from cmath import sqrt
import turtle
import math

pen = turtle.Turtle()
turtle.Screen().bgcolor('black')
pen.pencolor('white')
pen.speed(0)


def letter_a(points):
    pen.setheading(360)
    pen.width(2)
    pen.left(90)
    pen.forward(6 * points)  # 60
    pen.backward(6 * points)  # 60

    pen.width(1)
    pen.up()
    pen.right(90)
    pen.forward(2 * points)  # 20
    pen.down()
    pen.left(90)
    pen.forward(7 * points)  # 70
    pen.backward(7 * points)  # 70

    pen.width(2)
    pen.up()
    pen.right(90)
    pen.forward(2 * points)  # 20
    pen.down()
    pen.left(90)
    pen.forward(8 * points)  # 80

    line = math.sqrt((((4 * points) ** 2) + ((2 * points) ** 2)))  # 40, 20
    print(line)

    line_angle = math.degrees(math.acos((4 * points)/line))  # 40

    print(line_angle)
    pen.left(line_angle+90)
    pen.forward(line)
    pen.width(2)
    pen.right(line_angle+180+line_angle)
    pen.forward(line)


pen.up()
pen.setheading(180+90)
pen.forward(100)
pen.down()
letter_a(40)

pen.hideturtle()


turtle.done()

x = 100
angle1 = 45
angle2 = 45
angle3 = 90


# pen.left(angle1)
# print(f"start{pen.pos()}")
# pen.forward(x)
# print(f"1{pen.pos()}")
# pen.right(angle2+90)
# pen.forward(x * math.sin(math.radians(angle1)))
# pen.write(pen.pos())
# print(f"2{pen.pos()}")
# pen.right(angle3)
# pen.forward(x * math.cos(math.radians(angle1)))
# print(f"3{pen.pos()}")
