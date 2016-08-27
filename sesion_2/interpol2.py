from matrices import *

def mat_vec(mat):
    return (mat[0][0], mat[1][0], mat[2][0])

def solve3(A, b):
    return mat_vec(mul_mat(inv_mat(A), [[b[0]], [b[1]], [b[2]]]))

A = [[1, 2, 3], [4, 3, 1], [5, 2, 6]]
b = [3, 5, 6]

print solve3(A, b)

def lin2(x0, y0, x1, y1, x2, y2, x):
    A = [
        [x0 ** 2, x0, 1],
        [x1 ** 2, x1, 1],
        [x2 ** 2, x2, 1]
    ]

    B = [y0, y1, y2]

    (a, b, c) = solve3(A, B)

    return a * x ** 2 + b * x + c

for x in range(-10, 10):
    print x, lin2(0, 1, 1, 0, 2, 1, x)

def interpol2(P, x):
    n = len(P)

    for k in range(0, n - 2, 2):
        x0, y0 = P[k]
        x1, y1 = P[k + 1]
        x2, y2 = P[k + 2]
        if x < x2:
            return lin2(x0, y0, x1, y1, x2, y2, x)

    return lin2(x0, y0, x1, y1, x2, y2, x)

print "#######################"
for x in range(1, 17):
    print x, interpol2([(1, 1), (5, 4), (7, 2), (8, 10), (9, 15), (16, 7)], x)


