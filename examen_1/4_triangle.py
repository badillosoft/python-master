import turtle

class Triangle:

	def __init__(self, x0, y0, x1, y1, x2, y2):
		self.ax = x0
		self.ay = y0
		self.bx = x1
		self.by = y1
		self.cx = x2
		self.cy = y2
		self.color = "red"

		self.tur = turtle.Turtle()
		self.tur.ht()

	def contains(self, x, y):
		ax = self.cx - self.ax
		ay = self.cy - self.ay
		
		bx = self.bx - self.ax
		by = self.by - self.ay
		
		cx = x - self.ax
		cy = y - self.ay

		daa = ax * ax + ay * ay
		dab = ax * bx + ay * by
		dac = ax * cx + ay * cy

		dbb = bx * bx + by * by
		dbc = bx * cx + by * cy

		d = daa * dbb - dab * dab

		t = (dbb * dac - dab * dbc) / d
		s = (daa * dbc - dab * dac) / d

		return t >= 0 and s >= 0 and (t + s) <= 1.0

	def draw(self):
		# self.tur.st()
		self.tur.ht()
		self.tur.color("blue")
		self.tur.up()
		self.tur.goto(self.ax, self.ay)
		self.tur.down()
		self.tur.goto(self.bx, self.by)
		self.tur.goto(self.cx, self.cy)
		self.tur.goto(self.ax, self.ay)
		self.tur.up()
		self.tur.ht()

tri = Triangle(0, 0, 100, 50, 0, 100)

tri.draw()

def draw_dot(xo, yo):
	color = "red"

	if tri.contains(xo, yo):
		color = "green"

	tur = turtle.Turtle()
	tur.up()
	tur.goto(xo, yo)
	tur.down()
	tur.dot(5, color)
	tur.ht()

turtle.getscreen().onclick(draw_dot)

turtle.mainloop()