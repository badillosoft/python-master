import math
import matplotlib.pyplot as plot

class Robot:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t

    def mover(self, d):
        self.x += d * math.cos(self.t)
        self.y += d * math.sin(self.t)

    def girar(self, dt):
        self.t += (dt * math.pi) / 180.0

    def dibujar(self):
        plot.scatter(self.x, self.y)

r = Robot(10, 2, 0)

plot.ion()

while True:
    #plot.clf()
    plot.axis([-100, 100, -100, 100])
    plot.autoscale(False)
    r.mover(1)
    r.girar(2)
    r.dibujar()
    plot.pause(0.001)
    #r.log()
