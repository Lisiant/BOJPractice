import sys
from collections import deque

input = lambda: sys.stdin.readline()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def print_arr(arr):
    print()
    for i in range(n):
        print(*arr[i])


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
vis = [[0] * n for _ in range(n)]
s, x, y = map(int, input().split())


def append_virus():
    tmp = list()

    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0 and vis[i][j] == 0:
                tmp.append((grid[i][j], i, j))
                vis[i][j] = grid[i][j]

    tmp.sort()
    return deque(tmp)


def simulate(q: deque):
    while q:
        virus_num, x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny):
                continue

            if grid[nx][ny] != 0:
                continue

            grid[nx][ny] = virus_num


for i in range(s):
    q = append_virus()
    if not q:
        break
    simulate(q)

print(grid[x - 1][y - 1])
