import turtle
# reference: https://replit.com/talk/challenge/How-to-draw-Pixel-Art-on-Python-with-Turtle/7556

wn = turtle.Screen()
# setup the screen size - width, height
wn.setup(1200, 1200)
# change the colour
wn.bgcolor("Black")
# create the turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(4)


def square():
    for x in range(4):
        t.forward(20)
        t.right(90)


def tetris_piece_1():
    for x in range(4):
        t.begin_fill()
        square()
        t.color("Blue")
        t.end_fill()
        t.color("Black")
        t.forward(20)


tetris_piece_1()

t.penup()
t.forward(100)
t.pendown()


def tetris_piece_2():
    for x in range(4):
        t.begin_fill()
        square()
        t.color("Yellow")
        t.end_fill()
        t.color("Black")
        t.right(90)


tetris_piece_2()

t.penup()

t.right(90)

t.forward(100)

t.pendown()


def pac_man():
    for x in range(3):
        t.begin_fill()
        square()
        t.forward(20)
        t.color("Yellow")
        t.end_fill()
        t.color("Black")
    t.forward(20)
    t.right(180)
    for x in range(5):
        t.begin_fill()
        square()
        t.forward(20)
        t.color("Yellow")
        t.end_fill()
        t.color("Black")

    t.right(90)
    t.forward(40)
    t.right(90)
    for x in range(1):
        t.begin_fill()
        square()
        t.forward(20)
        t.color("Yellow")
        t.end_fill()
        t.color("Black")
    t.begin_fill()
    square()
    t.forward(20)
    t.color("Brown")
    t.end_fill()
    t.color("Black")
    t.begin_fill()
    square()
    t.forward(20)
    t.color("Yellow")
    t.end_fill()
    t.color("Black")
    t.begin_fill()
    square()
    t.forward(20)
    t.color("Yellow")
    t.end_fill()
    t.color("Black")
    t.begin_fill()
    square()
    t.forward(20)
    t.color("Yellow")
    t.end_fill()
    t.color("Black")
    t.right(180)
    t.begin_fill()
    square()
    t.forward(20)
    t.color("Yellow")
    t.end_fill()
    t.color("Black")
    t.begin_fill()
    square()
    t.forward(20)
    t.color("Yellow")
    t.end_fill()
    t.color("Black")
    t.penup()
    t.forward(20)
    t.pendown()
    t.begin_fill()
    square()
    t.forward(20)
    t.color("Yellow")
    t.end_fill()
    t.color("Black")
    t.begin_fill()
    square()
    t.forward(20)
    t.color("Yellow")
    t.end_fill()
    t.color("Black")
    t.right(90)
    t.forward(20)
    t.begin_fill()
    square()
    t.color("Yellow")
    t.end_fill()
    t.color("Black")
    t.right(90)
    t.penup()
    t.forward(80)
    t.pendown()
    t.left(90)
    t.begin_fill()
    square()
    t.color("Yellow")
    t.end_fill()
    t.color("Black")


for x in range(4):
    pac_man()
    t.forward(100)
    tetris_piece_2()
    t.forward(100)

t.forward(300)

tetris_piece_2()
pac_man()

turtle.done()
