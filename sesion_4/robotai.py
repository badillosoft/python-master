from robot import Robot
import matplotlib.pyplot as plot
import math

class RobotAI(Robot):
    def seguir(self, xo, yo):
        ux = math.cos(self.t)
        uy = math.sin(self.t)

        vx = xo - self.x
        vy = yo - self.y

        d = ux * vx + uy * vy
        r = (vx**2 + vy**2)**0.5

        if d >= r:
            self.girar(-0.8)
        elif d < r:
            self.girar(0.8)

        if abs(math.acos(d / r)) <= 0.8:
            self.mover(0.1)
        else:
            self.mover(0.01)

if __name__ == "__main__":
    xo = -5
    yo = 4

    r = RobotAI(0, 0, 0)

    # plot.ion()

    while True:
        # plot.clf()
        plot.axis([-10, 10, -10, 10])
        plot.autoscale(False)
        r.seguir(xo, yo)
        plot.scatter(xo, yo)
        r.dibujar()
        plot.pause(0.00001)
        #r.log()