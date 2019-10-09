def sort(A, sort_desc):
    if sort_desc:
        desc_sort(A)
    else:
        asc_sort(A)

def asc_sort(A):
    for i in range(1, len(A)):
        loc = i - 1
        item = A[i]
        while loc >= 0 and item < A[loc]:
            A[loc + 1] = A[loc]
            loc -= 1
        A[loc + 1] = item

def desc_sort(A):
    for i in range(1, len(A)):
        loc = i - 1
        item = A[i]
        while loc >= 0 and item > A[loc]:
            A[loc + 1] = A[loc]
            loc -= 1
        A[loc + 1] = item
