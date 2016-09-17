s = raw_input("Entrada: ")

aux = [c for c in s]

print "Salida:",

for i in range(1, len(aux) + 1):
	print aux[-i],

# inline program:
# print "Salida:", "".join(raw_input("Entrada: ")[::-1])