def lin(x0, y0, x1, y1, x):
    return y0 + float(y1 - y0) / (x1 - x0) * (x - x0)

#for x in range(-100, 100, 10):
#    print x, lin(1, 1, 5, 8, x)

def interpol(P, x):
    n = len(P)

    for k in range(0, n - 1):
        x0, y0 = P[k]
        x1, y1 = P[k + 1]
        if x < x1:
            return lin(x0, y0, x1, y1, x)

    return lin(x0, y0, x1, y1, x)

for x in range(0, 15):
    print x, interpol([(1, 1), (5, 5), (8, 6), (10, 2)], x)