import sys

input = lambda: sys.stdin.readline()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def solve(r, c, area_num):


    stk = [(r, c)]
    vis[r][c] = area_num

    while stk:
        x, y = stk.pop()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny):
                continue

            if graph[nx][ny] == 0:
                continue

            if vis[nx][ny] != 0:
                continue

            vis[nx][ny] = area_num
            stk.append((nx, ny))

def check_cnt(area_num):
    cnt = 0

    for i in range(n):
        for j in range(m):
            if vis[i][j] == area_num:
                cnt += 1

    return cnt


n, m, k = map(int, input().split())
coordinates = []
max_val = 0
area_num = 1
graph = [[0] * m for _ in range(n)]
vis = [[0] * m for _ in range(n)]
for i in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and vis[i][j] == 0:
            solve(i, j, area_num)
            cnt = check_cnt(area_num)
            max_val = max(max_val, cnt)
            area_num += 1

print(max_val)