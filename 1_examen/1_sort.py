s = raw_input("Entrada: ")

aux = s.split(' ')

a, b, c = int(aux[0]), int(aux[1]), int(aux[2])

# print "@", a, b, c

print "Salida:",

if a > b and a > c:
	if b > c:
		print c, b, a
	else:
		print b, c, a
elif b > a and b > c:
	if a > c:
		print c, a, b
	else:
		print a, c, b
else:
	if a > b:
		print b, a, c
	else:
		print a, b, c