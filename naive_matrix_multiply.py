def naive_matrix_multiply(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)
    C = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            s = 0
            for k in range(p):
                s += A[i][k]*B[k][j]
            C[i][j] = s
    return C
