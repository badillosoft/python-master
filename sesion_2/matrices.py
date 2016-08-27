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
