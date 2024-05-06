import sys

input = lambda: sys.stdin.readline()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
min_r, max_r, min_c, max_c = 100, 0, 100, 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


n, m = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]
temp = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        cnt = 0

        if grid[i][j] == 'X':

            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]

                if not in_range(nx, ny):
                    cnt += 1
                    continue

                if grid[nx][ny] == '.':
                    cnt += 1

            if cnt >= 3:
                temp[i][j] = True

for i in range(n):
    for j in range(m):
        if temp[i][j]:
            grid[i][j] = '.'

        elif grid[i][j] == 'X':
            min_r, max_r = min(min_r, i), max(max_r, i)
            min_c, max_c = min(min_c, j), max(max_c, j)

for i in range(min_r, max_r + 1):
    for j in range(min_c, max_c + 1):
        print(grid[i][j], end='')
    print()
