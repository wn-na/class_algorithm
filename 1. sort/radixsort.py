from math import log

def getdigit(num, k, base):
    return num % pow(base,k) // pow(base,k-1)

def stable_sort(a, k, base):
    n = len(a)
    b = [0] * base
    c = [0] * n
    for i in range(n):
        b[getdigit(a[i], k, base)] += 1
        
    for i in range(1, base):
        b[i] += b[i-1]

    for i in range(n - 1, -1 , -1):
        c[b[getdigit(a[i], k, base)] - 1] = a[i]
        b[getdigit(a[i], k, base)] -= 1

    for i in range(n):
        a[i] = c[i]

def radix_sort(a, base, sort_desc):
    k = int(log(max(a) + 1, base) + 1)
    for i in range(1, k + 1):
        stable_sort(a, i, base)

    if sort_desc:
        a.reverse()
        
def sort(A, sort_desc):
    DEFAULT_BASE = 10
    radix_sort(A, DEFAULT_BASE, sort_desc)
