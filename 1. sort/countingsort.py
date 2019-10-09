def sort(A, sort_desc):
    if sort_desc:
        desc_sort(A)
    else:
        asc_sort(A)
        
def asc_sort(a):
    k = max(a)
    n = len(a)
    b = [0] * (max(k, n)+1)
    c = [0] * (max(k, n)+1)
    
    for i in range(n):
        c[a[i]] += 1
        
    for i in range(1, k+1):
        c[i] += c[i-1]
        
    for i in range(n - 1, -1, -1):
        b[c[a[i]] - 1] = a[i]
        c[a[i]] -= 1
        
    for i in range(n):
        a[i] = b[i]
        
def desc_sort(a):
    k = max(a)
    n = len(a)
    b = [0] * (max(k, n)+1)
    c = [0] * (max(k, n)+1)
    
    for i in range(n):
        c[a[i]] += 1
        
    for i in range(1, k+1):
        c[i] += c[i-1]
        
    for i in range(n - 1, -1, -1):
        b[c[a[i]] - 1] = a[i]
        c[a[i]] -= 1
        
    for i in range(n):
        a[i] = b[n - 1 - i]
