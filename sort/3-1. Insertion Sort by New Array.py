def insertion_sort_newarray(arr):
    new_arr = [arr[0]]
    for i in range(1, len(arr)):
        loc = i-1
        item = arr[i]
        while loc >= 0 and item < new_arr[loc]:
            loc = loc - 1
        new_arr.insert(loc+1, item)
        print(new_arr)
    return new_arr

testcase = [3,31,48,73,8,11,20,29,65,15]
print("Insertion Sort by New Array", insertion_sort_newarray(testcase))
