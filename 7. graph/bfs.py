import queue

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(n):
    visited = [[False] * n for i in range(n)]
    q = queue.Queue()
    q.put((0, 0))
    while q.qsize():
        u = q.get()
        for i in range(4):
            ax = u[0] + dx[i]
            ay = u[1] + dy[i]
            if (ax >= 0 and ax < n) and (ay >= 0 and ay < n) and visited[ax][ay] == False:
                visited[ax][ay] = True
                q.put((ax, ay))

