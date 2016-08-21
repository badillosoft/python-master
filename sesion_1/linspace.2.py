import math

def linspace(a, b, n):
    if n <= 1:
        return [(a + b) / 2.0]

    vec = []

    delta = (b - a) / float(n - 1)

    #x = a
    #while x <= b:
    #    vec.append(x)
    #    x += delta

    for i in range(0, n):
        vec.append(a + i * delta)

    return vec

def linfun(space, f):
    vec = []

    for x in space:
        vec.append(f(x))

    return vec

def plot(X, Y):
    n = len(X)
    m = len(Y)
    r = min(n, m)

    for i in range(0, r):
        print X[i], Y[i]

X = linspace(-math.pi, math.pi, 120)

Y = linfun(X, math.sin)

plot(X, Y)