def sort(A, sort_desc):
    if sort_desc:
        desc_sort(A)
    else:
        asc_sort(A)

def asc_sort(A):
    for i in range(len(A) - 1, 0, -1):
        for j in range(0, i):
            if A[j] > A[j + 1]:
               A[j], A[j + 1] = A[j + 1], A[j]

def desc_sort(A):
    for i in range(len(A) - 1, 0, -1):
        for j in range(0, i):
            if A[j] < A[j + 1]:
               A[j], A[j + 1] = A[j + 1], A[j]
