def counting_sort(a, n, k):
    b = [0] * n
    c = [0] * n
    for i in range(n):
        c[a[i]] += 1
    for i in range(1, k+1):
        c[i] += c[i-1]
    for i in range(n - 1, -1, -1):
        b[c[a[i]] - 1] = a[i]
        c[a[i]] -= 1
    return b


testcase = [1,1,1,3,5,2,2,2,6,4,2,1]
print("Counting Sort", counting_sort(testcase, len(testcase), 6))
