import sys
from collections import deque

input = lambda: sys.stdin.readline()
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
vis = [[-1] * n for _ in range(n)]
res = 0
baby = [0, 0, 2, 2]  # x좌표, y좌표, 현재 크기, 성장 시까지 남은 섭취량



def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def init():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 9:
                baby[0], baby[1] = i, j
                return


def move(x, y):
    global res

    grid[baby[0]][baby[1]] = 0
    res += vis[x][y]
    baby[0], baby[1] = x, y

    if baby[3] == 1:
        baby[2] += 1
        baby[3] = baby[2]
    else:
        baby[3] -= 1

    for i in range(n):
        for j in range(n):
            vis[i][j] = -1


def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    vis[sx][sy] = 0
    temp = []

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny):
                continue

            if vis[nx][ny] != -1:
                continue

            if grid[nx][ny] > baby[2]:
                continue

            if grid[nx][ny] != 0 and grid[nx][ny] < baby[2]:
                temp.append((vis[x][y] + 1, nx, ny))

            q.append((nx, ny))
            vis[nx][ny] = vis[x][y] + 1

    return temp


def simulate():
    global res

    init()
    eatable = bfs(baby[0], baby[1])

    while eatable:
        eatable.sort(reverse=True)
        dist, pop_x, pop_y = eatable.pop()
        move(pop_x, pop_y)
        eatable = bfs(baby[0], baby[1])


simulate()
print(res)