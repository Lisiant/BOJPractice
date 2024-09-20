import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(str, input().rstrip())) for _ in range(n)]
vis = [[0] * m for i in range(n)]
res = 0


def bfs(x, y):
    global res

    q = deque()
    q.append((x, y))
    vis[x][y] = 1

    while q:

        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny):
                continue

            if vis[nx][ny]:
                continue

            if grid[nx][ny] == 'W':
                continue

            vis[nx][ny] = vis[x][y] + 1
            q.append((nx, ny))



def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def check_max_val(vis):
    cnt = 0
    for i in range(n):
        for j in range(m):
            cnt = max(cnt, vis[i][j])
    return cnt


for i in range(n):
    for j in range(m):
        if grid[i][j] == 'L':
            bfs(i, j)
            res = max(res, check_max_val(vis))

            vis = [[0] * m for i in range(n)]

print(res-1)