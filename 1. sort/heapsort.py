def sort(A, sort_desc):
    n = len(A) - 1
    buildHeap(A, n, sort_desc)
    for i in range(n, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i - 1, sort_desc)

def heapify(A, k, n, sort_desc):
    left = 2 * k
    right = 2 * k + 1

    smaller = 0
    if right <= n:
        if sort_desc:
            if A[left] < A[right]:
                smaller = left
            else:
                smaller = right
        else:
            if A[left] > A[right]:
                smaller = left
            else:
                smaller = right
    elif left <= n:
        smaller = left
    else:
        return
    
    if sort_desc:
        if A[smaller] < A[k]:
            A[k], A[smaller] = A[smaller], A[k]
            heapify(A, smaller, n, sort_desc)
    else:
        if A[smaller] > A[k]:
            A[k], A[smaller] = A[smaller], A[k]
            heapify(A, smaller, n, sort_desc)
            
def buildHeap(A, n, sort_desc):
    for i in range(int(n / 2), -1, -1):
        heapify(A, i, n, sort_desc)
