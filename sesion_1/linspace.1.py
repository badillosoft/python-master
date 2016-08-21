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

X = linspace(-math.pi, math.pi, 12)

Y = linfun(X, math.sin)

print X
print Y

