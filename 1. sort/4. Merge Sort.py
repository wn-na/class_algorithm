def merge_sort(arr, p, r):
    if p < r :
        q = int((p+r)/2)
        merge_sort(arr, p,q)
        merge_sort(arr, q+1, r)
        merge(arr,p,q,r)

def merge(arr, p, q, r):
    i = p
    j = q + 1
    tmp = []
    
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i+=1
        else:
            tmp.append(arr[j])
            j+=1

    while i<=q:
        tmp.append(arr[i])
        i+=1
    while j<=r:
        tmp.append(arr[j])
        j+=1
                
    i = p
    t = 0
    while i <= r:
        arr[i] = tmp[t]
        t+=1
        i+=1

testcase = [3,31,48,73,8,11,20,29,65,15]
merge_sort(testcase,0,len(testcase) - 1)
print("Merge Sort", testcase)
