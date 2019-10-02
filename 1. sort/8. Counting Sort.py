def counting_sort(a):
    k = max(a)
    n = len(a)
    b = [0] * n
    c = [0] * n
    
    for i in range(n):
        c[a[i]] += 1
        
    for i in range(1, k+1):
        c[i] += c[i-1]
        
    for i in range(n - 1, -1, -1):
        b[c[a[i]] - 1] = a[i]
        c[a[i]] -= 1
        
    for i in range(n):
        a[i] = b[i]

testcase = [1,1,1,3,5,2,2,2,6,4,2,1]
counting_sort(testcase)
print("Counting Sort", testcase)
