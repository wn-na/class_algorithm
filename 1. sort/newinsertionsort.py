def sort(A, sort_desc):
    if sort_desc:
        desc_sort(A)
    else:
        asc_sort(A)
        
def asc_sort(A):
    new_arr = [A[0]]
    for i in range(1, len(A)):
        loc = i - 1
        item = A[i]
        while loc >= 0 and item < new_arr[loc]:
            loc -= 1
        new_arr.insert(loc + 1, item)
    for i in range(len(new_arr)):
        A[i] = new_arr[i]

def desc_sort(A):
    new_arr = [A[0]]
    for i in range(1, len(A)):
        loc = i - 1
        item = A[i]
        while loc >= 0 and item > new_arr[loc]:
            loc -= 1
        new_arr.insert(loc + 1, item)
    for i in range(len(new_arr)):
        A[i] = new_arr[i]
