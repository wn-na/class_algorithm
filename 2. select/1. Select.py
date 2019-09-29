# 1.sort -> 5. Quick Sort
def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
           i+=1
           arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]

    return i + 1

def select(A, p, r, i):
    if p == r:
        return A[p]
    q = partition(A,p,r)
    k = q - p + 1
    if i < k:
        return select(A , p , q-1, i)
    elif i == k:
        return A[q]
    else:
        return select(A, q+1, r, i-k)


testcase = [3,31,48,73,8,11,20,29,65,15]
num = int(input("select n : "))
print("Select", select(testcase, 0, len(testcase) - 1, num))
