import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
res = []
cnt = 0


def check(lx, ly, rx, ry):
    for i in range(m - ry, m-ly):
        for j in range(lx, rx):
            graph[i][j] = 9


def bfs(a, b):
    q = deque()
    q.append((a, b))
    graph[a][b] = 1
    area = 0

    while q:
        x, y = q.popleft()
        area += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if graph[nx][ny] == 9 or graph[nx][ny] == 1:
                continue

            graph[nx][ny] = 1
            q.append((nx, ny))

    res.append(area)


for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    check(lx, ly, rx, ry)

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            bfs(i, j)
            cnt += 1

print(cnt)
res.sort()
for i in range(len(res)):
    print(res[i], end=' ')
