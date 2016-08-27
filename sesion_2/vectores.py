import math

#print math.sqrt(x), x ** 0.5

def add_vec(a, b):
    n = len(a)
    c = [0] * n

    for i in range(0, n):
        c[i] = a[i] + b[i]

    return c

def sub_vec(a, b):
    n = len(a)
    c = [0] * n

    for i in range(0, n):
        c[i] = a[i] - b[i]

    return c

def mul_vec(e, u):
    n = len(u)
    v = [0] * n

    for i in range(0, n):
        v[i] = u[i] * e

    return v

def dot_vec(a, b):
    n = len(a)
    s = 0

    for i in range(0, n):
        s = s + a[i] * b[i]

    return s

def times_vec(a, b):
    return [
        a[1] * b[2] - a[2] * b[1],
        -(a[0] * b[2] - a[2] * b[0]),
        a[0] * b[1] - a[1] * b[0] 
    ]

def norm_vec(u):
    return dot_vec(u, u) ** 0.5

def unit(u):
    return mul_vec(1.0 / norm_vec(u), u)

def proj_vec(a, b):
    return mul_vec(norm_vec(a), unit(b)) 