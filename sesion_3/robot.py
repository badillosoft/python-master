import math

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

r = Robot(10, 2, 0)

r.log()
r.mover(10)
r.log()
