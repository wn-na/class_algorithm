def nativematching(a, p):
    n = len(a)
    m = len(p)
    for i in range(n - m):
        flag = False
        for j in range(m):
            if a[i + j] != p[j]:
                flag = True
                break
        if flag is False:
            return i
    return None

if __name__ == "__main__":
    a = "boboycatsoaropt"
    p = "soar"
    where = nativematching(a, p)
    print(where)
    print(a[where : where + len(p)])
