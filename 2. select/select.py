def partition(A, p, r):
    x = A[r - 1]
    i = p
    for j in range(p, r - 1):
        if A[j] <= x:
           A[i], A[j] = A[j], A[i]
           i += 1
    A[i], A[r - 1] = A[r - 1], A[i]
    return i

def select(A, p, r, i):
    if p == r:
        return A[p]
    q = partition(A, p, r)
    k = q - p 
    if i < k:
        return select(A, p, q, i)
    elif i == k:
        return A[q]
    else:
        return select(A, q + 1, r, i - k - 1)
