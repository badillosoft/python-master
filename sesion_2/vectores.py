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

def unit_vec(u):
    return mul_vec(1.0 / norm_vec(u), u)

def proj_vec(a, b):
    return mul_vec(norm_vec(a), unit_vec(b))

if __name__ == "__main__":
    print add_vec((1, 2, 3), (4, 5, 6))
    print sub_vec((1, 2, 3), (4, 5, 6))
    print mul_vec(2, (4, 5, 6))
    print dot_vec((1, 2, 3), (4, 5, 6))
    print times_vec((1, 2, 3), (4, 5, 6))
    print norm_vec((1, 2, 3))
    print unit_vec((1, 2, 3))
    print proj_vec((1, 2, 3), (4, 5, 6))