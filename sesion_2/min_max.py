def min_max(arreglo):
    if len(arreglo) < 1:
        return (None, None)

    min = arreglo[0]
    max = arreglo[0]

    for x in arreglo:
        if x < min:
            min = x
        elif x > max:
            max = x

    return (min, max)

print min_max([3, 5, 2, 4])

a = range(4, 79, 5)

print min_max(a)

print min_max([3, 2, 1])

(i, j) = min_max((4, 3, 5, 2, 8, 6))

print "Minimo", i, "Maximo", j