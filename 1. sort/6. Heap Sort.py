def heapify(A, k ,n):
    print("call heapify(",k,",",n,")")
    left = 2 * k
    right = 2 * k + 1

    smaller = 0
    if right <= n:
        if A[left] < A[right]:
            smaller = left
        else:
            smaller = right
    elif left <= n:
        smaller = left
    else:
        return

    #print("k:",k,"(",A[k],")"," left:",left,"(",A[left],")"," right:",right,"(",A[right],")", "data:", A)

    if A[smaller] < A[k]:
        A[k], A[smaller] = A[smaller], A[k]
        heapify(A,smaller,n)

def buildHeap(A, n):
    for i in range(int(n/2),-1, -1):
        print("buildHeap -> heapify n:",n,"/i:",i)
        heapify(A, i, n)

def heap_sort(A, n):
    buildHeap(A,n)
    print("=====buildHeap End===========")
    for i in range(n, 0, -1):
        A[0] , A[i] = A[i], A[0]
        heapify(A,0,i-1)
    return A

testcase = [3,31,48,73,8,11,20,29,65,15]
#print("buildHeap", buildHeap(testcase, len(testcase)-1), testcase)
print("Heap Sort", heap_sort(testcase, len(testcase) - 1))
