import turtle
import random

points = [
    (-100, 0, "red"),
    (-90, 10, "blue"),
    (-80, 34, "black"),
    (-70, 27, "purple"),
    (-60, -45, "red"),
    (-50, 61, "red"),
    (-40, 33, "pink"),
    (-30, 98, "red"),
    (-20, -45, "yellow"),
    (-10, 16, "red"),
    (0, 0, "red"),
    (10, 10, "red"),
    (20, 80, "blue"),
    (30, 100, "red"),
    (40, 60, "pink"),
    (50, 80, "yellow"),
    (60, 10, "red"),
    (70, 60, "blue"),
    (80, 10, "red"),
    (90, 80, "yellow"),
    (100, 60, "blue")
]

t1 = turtle.Turtle()

x, y, c = points[0]

t1.pu()
t1.setpos(x, y)
t1.pencolor(c)
t1.pd()

for x, y, c in points:
    t1.pencolor(c)
    t1.goto(x, y)

#t1.onrelease(turn)

turtle.mainloop()