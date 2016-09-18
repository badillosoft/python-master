import turtle
import random

class Robot(turtle.Turtle):

    def seguir(self, xo, yo):
        print self.xcor(), self.ycor()

sc = turtle.Screen()

t1 = Robot()

#t1.seguir(10, 50)

#for x, y in [(10, 20), (10, 40), (50, 30), (-100, 2)]:
#    t1.goto(x, y)
#    t1.speed(1)

def turn(x, y):

    print x, y

    left = random.choice([True, False])
    
    a = random.randint(0, 60)

    if left:
        t1.left(a)
    else:
        t1.right(a)

    t1.fd(10)

sc.onclick(turn)

#t1.onrelease(turn)

turtle.mainloop()