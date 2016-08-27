A = [
    [1, 2],
    [5, 3]
]

B = [
    [4, 2],
    [1, 3]
]

print A

def print_mat(mat):
    n = len(mat)
    m = len(mat[0])

    print "[%dx%d]" % (n, m)

    for vec in mat:
        print "  ",
        for x in vec:
            print x,
        print


print_mat(A)

def new_mat(n, m):
    mat = []

    for i in range(0, n):
        vec = []
        for j in range(0, m):
            vec.append(0)
        mat.append(vec)

    return mat

def trans_mat(A):
    n = len(A)
    m = len(A[0])

    B = new_mat(m, n)

    for i in range(0, n):
        for j in range(0, m):
            B[j][i] = A[i][j]

    return B

print_mat([[1, 2, 3], [4, 5, 6]])

print_mat(trans_mat([[1, 2, 3], [4, 5, 6]]))

print_mat(trans_mat(trans_mat([[1, 2, 3], [4, 5, 6]])))

def mul_mat(A, B):
    a, b = len(A), len(A[0])
    c, d = len(B), len(B[0])

    if b != c:
        print "Las matrices no se pueden multiplicar"
        return None

    C = new_mat(a, d)

    for i in range(0, a):
        for j in range(0, d):
            s = 0
            for k in range(0, b):
                s += A[i][k] * B[k][j]
            C[i][j] = s

    return C

print_mat(mul_mat(A, B))

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

def min_mat(A, i, j):
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

def adj_mat(A):
    n, m = len(A), len(A[0])
    B = new_mat(n, m)
    for i in range(0, n):
        for j in range(0, m):
            aux = min_mat(A, i, j)
            B[i][j] = ((-1) ** (i + j)) * det2(aux[0][0], aux[0][1], aux[1][0], aux[1][1])
    return B

def inv_mat(A):
    B = trans_mat(adj_mat(A))

    d = det3(A)

    n, m = len(B), len(B[0])

    for i in range(0, n):
        for j in range(0, m):
            B[i][j] = B[i][j] / float(d)

    return B

print_mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print_mat(min_mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))

A = [
    [1, 2, 3],
    [2, 4, 5],
    [1, 6, 2]
]

B = inv_mat(A)

print_mat(A)
print_mat(B)
print_mat(mul_mat(A, B))