def partition(A, p, r, x):
    i = -1
    for j in range(p, r):
      if A[j] == x:
        i = j
        A[r - 1], A[i] = A[i], A[r - 1]
        break

    idx = p

    for j in range(p, r - 1):
        if A[j] < x:
            A[j], A[idx] = A[idx], A[j]
            idx += 1
        
    if i != -1:
        A[idx], A[r-1] = A[r-1], A[idx]

    return idx

def select(A, p, r, i):
    groups = []

    for x in range(p, r):
        if (x - p) % 5 == 0:
            groups.append([])
        groups[((x - p) // 5)].append(A[x])

    for x in groups:
        x.sort()

    mid = []
    for x in groups:
        mid.append(x[(len(x) - 1) // 2])
        
    if len(mid) == 1:
        median = mid[0]
    else:
        median = select(mid, 0, len(mid), (len(mid) - 1) // 2)
    q = partition(A, p, r, median)
    
    if p + i < q:
        return select(A, p, q, i)
    if p + i > q:
        return select(A, q + 1, r, p + i - q - 1)
    return A[p + i]
