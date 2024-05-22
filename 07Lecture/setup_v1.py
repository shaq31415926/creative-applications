from turtle import *

speed(10) # set cursor to the fastest speed

# change size of screen
screensize(canvwidth=400,
           canvheight=300,
           bg="blue")

color('blue', 'yellow')
begin_fill()

while True:
    forward(200)
    left(170)
    #print(pos())
    if abs(pos()) < 1:
        break

end_fill()
done()
