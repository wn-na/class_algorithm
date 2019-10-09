def theLargest(A, i):
    select = 0
    for j in range(1, i + 1):
        if A[j] >= A[select]:
            select = j
    return select

def theSmallest(A, i):
    select = 0
    for j in range(1, i + 1):
        if A[j] <= A[select]:
            select = j
    return select

def sort(A, sort_desc):
    for i in range(len(A) - 1, 0, -1):
        if sort_desc:
            select = theSmallest(A, i)
        else:
            select = theLargest(A, i)
        A[i], A[select] = A[select], A[i]

