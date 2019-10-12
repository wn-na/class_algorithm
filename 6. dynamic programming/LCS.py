x = "CDABE"
y = "CDEGT"

def recu_lcs(m, n):
    if m == -1 or n == -1:
        return 0
    elif x[m] == y[n]:
        return recu_lcs(m - 1, n - 1) + 1
    else:
        return max(recu_lcs(m - 1, n), recu_lcs(m, n - 1))

def lcs(m, n):
    c = [[0] * (m + 1)] * (n + 1)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i][j - 1], c[i - 1][j])
    return c[m][n]

if __name__ == "__main__":
    print(recu_lcs(len(x) - 1, len(y) - 1))
    print(lcs(len(x), len(y)))
