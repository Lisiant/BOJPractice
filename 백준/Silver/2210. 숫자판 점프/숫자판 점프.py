import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

input = lambda: sys.stdin.readline()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
grid = [list(map(str, input().split())) for _ in range(5)]

dic = defaultdict()


def in_range(nx, ny):
    return 0 <= nx < 5 and 0 <= ny < 5


def dfs(x, y, cur, depth):
    if depth == 6:
        dic[cur] = 1
        return

    if not in_range(x, y):
        return

    s = cur + grid[x][y]

    dfs(x - 1, y, s, depth + 1)
    dfs(x + 1, y, s, depth + 1)
    dfs(x, y - 1, s, depth + 1)
    dfs(x, y + 1, s, depth + 1)


for i in range(5):
    for j in range(5):
        dfs(i, j, '', 0)
print(len(dic.keys()))
