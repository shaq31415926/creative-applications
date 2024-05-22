from turtle import *

speed(0) # set cursor to the fastest speed

color('blue', 'yellow')
begin_fill()

for i in range(10):
    circle(40)
    right(36)

# change size of screen
screensize(canvwidth=400,
           canvheight=300,
           bg="blue")

end_fill()
done()
