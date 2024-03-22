import sys
from collections import deque

input = lambda: sys.stdin.readline()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
grid = [list(map(str, input().rstrip())) for _ in range(n)]
vis = [[0] * m for _ in range(n)]
fr, en = 0, 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs_fr(sx, sy):
    temp = 1

    q = deque()
    q.append((sx, sy))
    vis[sx][sy] = 1

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny):
                continue

            if vis[nx][ny] != 0:
                continue

            if grid[nx][ny] != 'W':
                continue

            temp += 1
            vis[nx][ny] = 1
            q.append((nx, ny))

    return temp


def bfs_en(sx, sy):
    temp = 1

    q = deque()
    q.append((sx, sy))
    vis[sx][sy] = 1

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny):
                continue

            if vis[nx][ny] != 0:
                continue

            if grid[nx][ny] != 'B':
                continue

            temp += 1
            vis[nx][ny] = 2
            q.append((nx, ny))

    return temp


for i in range(n):
    for j in range(m):
        if grid[i][j] == 'W' and vis[i][j] == 0:
            fr += (bfs_fr(i, j) ** 2)

        if grid[i][j] == 'B' and vis[i][j] == 0:
            en += (bfs_en(i, j) ** 2)

print(fr, en)
