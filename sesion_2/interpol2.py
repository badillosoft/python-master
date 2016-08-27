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

    return a00 * det2(a11, a12, a21, a22)
        - a01 * det2(a10, a12, a20, a22)
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
            B[i][j] = A[]
