from matrices import *

def det2(a, b, c, d):
    return a * d - b * c

def det3(mat):
    a00 = mat[0][0]
    a01 = mat[0][1]
    a02 = mat[0][2]
    
    a10 = mat[1][0]
    a11 = mat[1][1]
    a12 = mat[1][2]
    
    a20 = mat[2][0]
    a21 = mat[2][1]
    a22 = mat[2][2]

    return a00 * det2(a11, a12, a21, a22) \
        - a01 * det2(a10, a12, a20, a22) \
        + a02 * det2(a10, a11, a20, a21)

def min(A, i, j):
    n, m = len(A), len(A[0])
    mat = []

    for a in range(0, n):
        if a == i:
            continue

        vec = []
        for b in range(0, m):
            if b == j:
                continue

            vec.append(A[a][b])
        
        mat.append(vec)

    return mat

def adj(A):
    n, m = len(A), len(A[0])
    B = new_mat(n, m)
    for i in range(0, n):
        for j in range(0, m):
            aux = min(A, i, j)
            B[i][j] = ((-1) ** (i + j)) * det2(aux[0][0], aux[0][1], aux[1][0], aux[1][1])
    return B

def inv(A):
    B = trans_mat(adj(A))

    d = det3(A)

    n, m = len(B), len(B[0])

    for i in range(0, n):
        for j in range(0, m):
            B[i][j] = B[i][j] / float(d)

    return B

print_mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print_mat(min([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))

A = [
    [1, 2, 3],
    [2, 4, 5],
    [1, 6, 2]
]

B = inv(A)

print_mat(A)
print_mat(B)
print_mat(mul_mat(A, B))