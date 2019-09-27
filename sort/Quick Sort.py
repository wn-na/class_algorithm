def quick_sort(arr, p, r):
    if p < r :
        q = partition(arr, p, r)
        quick_sort(arr, p,   q-1)
        quick_sort(arr, q+1, r)

def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
           i+=1
           arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]

    return i + 1

testcase = [3,31,48,73,8,11,20,29,65,15]
quick_sort(testcase,0,len(testcase) - 1)
print("Quick Sort", testcase)
