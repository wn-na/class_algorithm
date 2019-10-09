def sort(A, sort_desc):
    quick_sort(A, 0, len(A) - 1, sort_desc)

def quick_sort(A, p, r, sort_desc):
    if p < r :
        q = partition(A, p, r, sort_desc)
        quick_sort(A, p, q - 1, sort_desc)
        quick_sort(A, q + 1, r, sort_desc)

def partition(A, p, r, sort_desc):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if sort_desc:
            if A[j] >= x:
               i += 1
               A[i], A[j] = A[j], A[i]
        else:
            if A[j] <= x:
               i += 1
               A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]

    return i + 1
