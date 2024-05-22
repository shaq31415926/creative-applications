from turtle import *

t = Turtle()
t.speed(0)  # fastest speed

t.penup()
t.goto(-200, -100)  # changes the position of the cursor
t.pendown()

side_length = 30  # variable to define the length of the square


def create_square(square_colour, side_length):
    t.color(square_colour)
    t.begin_fill()
    # creates the square
    for num in range(4):
        t.forward(side_length)
        t.rt(90)
    t.end_fill()
    t.forward(side_length)


# loop through a list of colours and create squares
colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
#colours = ["red", "orange", "pink", "yellow"]

for c in colours:
    create_square(c, side_length)


def new_row(colours, side_length):
    t.penup()
    t.left(90)
    t.forward(side_length)
    t.left(90)
    #t.forward((len(colours)) * side_length)
    t.forward((len(colours)-1) * side_length)
    t.right(180)
    t.pendown()

#  create a row above
new_row(colours, side_length)
# CHALLENGE: create multiple row of squares
# create_square("blue")

for i in range(4):
    for c in colours:
        create_square(c, side_length)
    new_row(colours, side_length)
done()
