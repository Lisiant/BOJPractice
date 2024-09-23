from collections import deque
import sys

input = lambda: sys.stdin.readline()
INF = 987654321
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
grid = [[0] * 501 for _ in range(501)]
vis = [[0] * 501 for _ in range(501)]
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            grid[i][j] = 1

m = int(input())
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            grid[i][j] = 2

answer = INF


def bfs(sx, sy):
    global answer

    q = deque()

    vis[sx][sy] = 1
    q.append((sx, sy))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx >= 501 or nx < 0 or ny < 0 or ny >= 501:
                continue

            if vis[nx][ny] != 0 or grid[nx][ny] == 2:
                continue

            if grid[nx][ny] == 0:
                vis[nx][ny] = vis[x][y]
                q.appendleft((nx, ny))

            if grid[nx][ny] == 1:
                vis[nx][ny] = vis[x][y] + 1
                q.append((nx, ny))


bfs(0, 0)

if vis[500][500] == 0:
    print(-1)
else:
    print(vis[500][500] - 1)
