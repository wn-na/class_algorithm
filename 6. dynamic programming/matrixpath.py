# rule
# only move down and right
# not allow move up, left, diagonal

m = [[6, 7, 12, 5], [5, 3, 11, 18], [7, 17, 3, 3], [8, 10, 14, 9]]

def recu_matrixpath(i, j):
    if i == -1 or j == -1:
        return 0
    else:
        return m[i][j] + max(recu_matrixpath(i - 1, j), recu_matrixpath(i, j - 1))

def matrixpath(n):
    c = [[0] * (n + 1)] * (n + 1)
    for i in range(0, n):
        for j in range(0, n):
            c[i + 1][j + 1] = m[i][j] + max(c[i][j + 1], c[i + 1][j])
    return c[n][n]

if __name__ == "__main__":
    print(recu_matrixpath(3, 3))
    print(matrixpath(4))
