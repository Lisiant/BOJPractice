import sys
from collections import deque

input = lambda: sys.stdin.readline()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
grid = [list(map(str, input().rstrip())) for _ in range(n)]
vis = [[0] * m for _ in range(n)]
res = [0, 0]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(sx, sy):
    sheep, wolf = 0, 0
    q = deque()
    q.append((sx, sy))
    vis[sx][sy] = 1

    if grid[sx][sy] == 'v':
        wolf += 1
    elif grid[sx][sy] == 'o':
        sheep += 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny):
                continue

            if grid[nx][ny] == '#' or vis[nx][ny] != 0:
                continue

            if grid[nx][ny] == 'o':
                sheep += 1

            if grid[nx][ny] == 'v':
                wolf += 1

            vis[nx][ny] = 1
            q.append((nx, ny))

    return sheep, wolf


for i in range(n):
    for j in range(m):
        if grid[i][j] != '#' and vis[i][j] == 0:
            s, w = bfs(i, j)
            if s > w:
                res[0] += s
            else:
                res[1] += w

print(*res)

