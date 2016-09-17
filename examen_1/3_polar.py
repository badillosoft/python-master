import math

def polar(x, y):
	r = (x**2 + y**2)**0.5
	t = math.atan2(y, x)
	return (r, t)

s = raw_input("Entrada: ")

aux = s.split(' ')

x, y = float(aux[0]), float(aux[1])

print "Salida:", polar(x, y)
