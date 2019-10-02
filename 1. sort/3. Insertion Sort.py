def insertion_sort(arr):
    for i in range(1, len(arr)):
        loc = i-1
        item = arr[i]
        while loc >= 0 and item < arr[loc]:
            arr[loc + 1] = arr[loc]
            loc = loc - 1
        arr[loc+1] = item

testcase = [3,31,48,73,8,11,20,29,65,15]
insertion_sort(testcase)
print("Insertion Sort", testcase)
