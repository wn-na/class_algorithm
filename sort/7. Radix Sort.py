def stable_sort(a, n, k):
    b = [0] * 10
    c = [0] * n
    for i in range(n):
        b[a[i] % pow(10,k) // pow(10,k-1)] += 1
        
    for i in range(1, 10):
        b[i] += b[i-1]

    for j in range(n - 1, -1 , -1):
        c[b[a[j] % pow(10,k) // pow(10,k-1)] - 1] = a[j]
        b[a[j] % pow(10,k) // pow(10,k-1)] -= 1
    return c

def radix_sort(a, n, k):
    for i in range(1, k + 1):
        a = stable_sort(a, n, i)
    return a

testcase = [123,2154,222,4,223,1560,1061,2150]
print("radix Sort", radix_sort(testcase, len(testcase), 4))
