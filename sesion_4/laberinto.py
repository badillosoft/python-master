from turtle import *
import random

sc = Screen()

walls = [
    #(x0, y0, x1, y1)
    (10, 100, 20, 20),
    (100, 10, -20, -20),
    (70, 60, 50, -20),
    (-30, -10, -20, 20)
]

tw = Turtle()

for x0, y0, x1, y1 in walls:
    tw.pu()
    tw.goto(x0, y0)
    tw.pd()
    tw.goto(x1, y1)

tw.ht()

def distance_wall(x, y, walls):
    return random.randint(0, 100)

t = Turtle()

while True:
    if (distance_wall(t.xcor(), t.ycor(), walls) >= 1):
        t.fd(0.1)
    else:
        t.lt(30)

mainloop()