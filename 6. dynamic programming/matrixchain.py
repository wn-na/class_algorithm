# [3, 5], [5, 1], [1, 8]
p = [5, 3, 2, 6]

def recu_MatrixChain(i, j):
    if i == j:
        return 0
    val = 9999999
    for k in range(i, j):
        val = min(val, recu_MatrixChain(i, k) + recu_MatrixChain(k+1, j) + p[i-1] * p[k] * p[j])
    return val

def matrixchain(n):
    m = [ [9999999999] * (n + 1) for _ in range(n + 1)]
    for i in range(n+1):
        m[i][i] = 0
    for r in range(1, n):
        for i in range(1, n - r + 1):
            j = i + r
            for k in range(i, j):
                m[i][j] = min(m[i][j], m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j])
    return m[1][n]
    
if __name__ == "__main__":
    print(recu_MatrixChain(1, 3))
    print(matrixchain(len(p) - 1))
