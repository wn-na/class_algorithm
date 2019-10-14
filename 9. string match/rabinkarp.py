def basicrabinkarp(a, p, d):
    n = len(a)
    m = len(p)

    k = 0
    w = [0] * n

    alphatoint = lambda a : ord(a) - ord('a')
    for i in range(m):
        k = d * k + alphatoint(p[i])
        w[0] = d * w[0] + alphatoint(a[i])

    for i in range(0, n - m + 1):
        if i != 0:
            w[i] = d * (w[i - 1] - (alphatoint(a[i - 1]) * (d ** (m - 1)))) + alphatoint(a[i + m - 1])
        if k == w[i]:
            return i
    return None
        
if __name__ == "__main__":
    a = "acebbceeaabceedb"
    p = "eeaab"
    k = basicrabinkarp(a, p, 5)
    print(k)
    print(a[k:k+len(p)])
