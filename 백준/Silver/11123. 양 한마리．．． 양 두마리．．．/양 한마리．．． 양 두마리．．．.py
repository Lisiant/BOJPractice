import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(sx, sy, graph, vis):
    q = deque()
    q.append((sx, sy))
    vis[sx][sy] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny):
                continue

            if graph[nx][ny] == '.' or vis[nx][ny] != 0:
                continue

            vis[nx][ny] = 1
            q.append((nx, ny))


def check():
    res = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == '#' and vis[i][j] == 0:
                bfs(i, j, graph, vis)
                res += 1

    return res


t = int(input())
for i in range(t):
    cnt = 0
    n, m = map(int, input().split())
    graph = [list(map(str, input().rstrip())) for _ in range(n)]
    vis = [[0] * m for _ in range(n)]

    result = check()
    print(result)