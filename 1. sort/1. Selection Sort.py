def theLargest(arr, i):
    select = 0
    for j in range(1, i + 1):
        if arr[j] > arr[select]:
            select = j
    return select

def selection_sort(arr):
    for i in range(len(arr) - 1, 1, -1):
        select = theLargest(arr, i)
        arr[i], arr[select] = arr[select], arr[i]
    return arr

testcase = [3,31,48,73,8,11,20,29,65,15]
print("Selection Sort", selection_sort(testcase))
