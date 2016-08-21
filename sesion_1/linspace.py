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

print linspace(0, 1, 3)
print linspace(0, 1, 7)
print linspace(-10, 10, 14)