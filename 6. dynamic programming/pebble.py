a = [[6, -8, 11], [7, 10, 12], [12, 14, 7], [-5, 9, 4], [5, 7, 8], [3, 13, -2], [11, 8, 9], [3, 5, 4]]
w = [[0] * 4 for i in range(len(a) + 1)]
pat = [[1, 2],
       [0, 2, 3],
       [0,1],
       [1]]

def init():
    print(id(w[0][0]), id(w[1][0]))
    for i in range(len(a)):
        for j in range(4):
            w[i][j] = a[i][j % 3]
            if j == 3:
                w[i][j] += a[i][2]
            
def recu_pebble(i, p):
    if i == -1:
        return w[0][p]
    else:
        val = 0
        for q in range(0, 4):
            if q in pat[p]:
                val = max(val, recu_pebble(i - 1, q))
        return val + w[i][p]

def pebble(n):
    peb = [[0] * 4 for i in range(n + 1)]
    for p in range(4):
        peb[0][p] = w[0][p]
    for i in range(1, n + 1):
        for p in range(4):
            for q in pat[p]:
                peb[i][p] = max(peb[i - 1][q] , peb[i][p])
            peb[i][p] += w[i][p]
    return max(peb[n])

if __name__ == "__main__":
    init()
    print("recu_pebble 0 max is ", recu_pebble(len(a) - 1, 0))
    print("recu_pebble 1 max is ", recu_pebble(len(a) - 1, 1))
    print("recu_pebble 2 max is ", recu_pebble(len(a) - 1, 2))
    print("recu_pebble 3 max is ", recu_pebble(len(a) - 1, 3))
    print("pebble max is ", pebble(len(a)))
