import sys
from collections import deque
input = sys.stdin.readline


def init():
    xy = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                xy.append(i)
                xy.append(j)
    return xy


def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    vis[sx][sy] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 1 :
                continue
            
            if vis[nx][ny] >= 0:
               continue 
            
            if graph[nx][ny] == 3 or graph[nx][ny] == 4 or graph[nx][ny] == 5:
                return vis[x][y] + 1

            vis[nx][ny] = vis[x][y] + 1
            q.append((nx, ny))

    return -1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
vis = [[-1] * m for _ in range(n)]

start = init()
dist = bfs(start[0], start[1])

if dist != -1:
    print("TAK")
    print(dist)
else:
    print("NIE")
