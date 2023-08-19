import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

data = [list(map(int, input().rstrip())) for _ in range(n)]
vis = [[0] * m for _ in range(n)]
q = deque()
res = 0

q.append((0, 0))
vis[0][0] = 1

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if vis[nx][ny] != 0 or data[nx][ny] != 1:
            continue

        vis[nx][ny] = vis[x][y] + 1
        q.append((nx, ny))

print(vis[n - 1][m - 1])
