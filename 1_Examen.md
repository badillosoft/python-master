# Curso de Python

## Primer Exámen de conocimientos

Resuelva los siguientes problemas individualmente con el fin de comprobar sus conocimientos en _python_. El exámen no tiene ninguna ponderación en el curso y será resuelto una vez concluido.

## Parte I

### 1. Crear un programa que solicite tres números al usuario y mediante condiciones `if-elif-else` los imprima de manera ordenada.

~~~
Entrada: 3 1 2
Salida: 1 2 3
  
Entrada: 2 1 3
Salida: 1 2 3
~~~

### 2. Crear un programa que solicite un texto, luego recorra cada carácter del texto y lo guarde en un arreglo. Finalmente mediante un ciclo `for-in` o un ciclo `while` imprima el texto inverso, es decir, primero el último caráter y así sucesivamente hasta llegar al primero.

~~~
Entrada: "Hola Mundo"
Salida: "odnuM aloH"

Entrada: "Hey, como estas?"
Salida: "?satse omoc, yeH"
~~~

### 3. Crear un programa que defina la función `polar` la cual reciba un número `x` y un número `y` y devuelva una tupla `(r, t)` donde `r = √ (x^2 + y^2)` y `t = atan2(y, x)`.

~~~
Entrada: polar(1, 1)
Salida: (1.4142135623730951, 0.7853981633974483)

Entrada: polar(2, 3)
Salida: (3.605551275463989, 0.982793723247329)
~~~

## Parte II

### 4. La siguiente clase llamada `Triangle` se construye a partir de las coordenadas de 3 puntos y posee un método llamado `contains` para determinar si un punto está contenido dentro del triángulo. El método `draw` dibuja triángulo uniendo sus 3 vétices y colocando en el centro de este un punto verde si el punto objetivo está en él o rojo sino. Sin embargo la clase tiene algunos errores lógicos y de sintaxis. Resuleva los errores y ejecute el script para obtener los resultados esperados.

~~~py
import turtle

class Triangle:

	def _init_(self, x0, y0, x1, y1, x2, y2):
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

		#return t >= 0 and s >= 0 and (t + s) <= 1.0

	def draw():
		# self.tur.st()
		self.tur.ht()
		self.tur.color("blue")
		tur.up()
		self.tur.goto(self.ax, self.ay)
		self.tur.down()
		self.tur.goto(self.bx, self.by)
		self.tur.goto(self.cx, self.cy)
		self.tur.goto(self.ax, self.ay)
		self.tur.up()
		self.tur.ht()

tri = new Triangle(0, 0, 100, 50, 0, 100)

tri.draw()

def draw_dot(xo):
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
~~~
