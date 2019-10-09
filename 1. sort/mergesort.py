def sort(A, sort_desc):
    merge_sort(A, 0, len(A) - 1, sort_desc)

def merge_sort(A, p, r, sort_desc):
    if p < r :
        q = int((p + r) / 2)
        merge_sort(A, p, q, sort_desc)
        merge_sort(A, q + 1, r, sort_desc)
        if sort_desc:
            desc_merge(A, p, q, r)
        else:
            merge(A, p, q, r)

def merge(A, p, q, r):
    i = p
    j = q + 1
    tmp = []
    
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q:
        tmp.append(A[i])
        i += 1
    while j<=r:
        tmp.append(A[j])
        j += 1
                
    i = p
    t = 0
    while i <= r:
        A[i] = tmp[t]
        t += 1
        i += 1

def desc_merge(A, p, q, r):
    i = p
    j = q + 1
    tmp = []
    
    while i <= q and j <= r:
        if A[i] >= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1
                
    i = p
    t = 0
    while i <= r:
        A[i] = tmp[t]
        t += 1
        i += 1
