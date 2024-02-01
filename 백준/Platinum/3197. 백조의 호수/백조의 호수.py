import sys
from collections import deque
import copy

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


def find_swan():
    global is_finished

    while cur_swan:
        x, y = cur_swan.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny):
                continue

            if vis[nx][ny]:
                continue

            if graph[nx][ny] == '.':
                vis[nx][ny] = True
                cur_swan.append((nx, ny))

            if graph[nx][ny] == 'X':
                vis[nx][ny] = True
                next_swan.append((nx, ny))

            if graph[nx][ny] == 'L':
                vis[nx][ny] = True
                is_finished = True
                break


def find_melt():
    while cur_water:
        x, y = cur_water.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny):
                continue

            if graph[nx][ny] == 'X':
                graph[nx][ny] = '.'
                next_water.append((nx, ny))


r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
swan_x, swan_y = 0, 0
res = 0
is_finished = False
cur_swan, next_swan = deque(), deque()
cur_water, next_water = deque(), deque()

for i in range(r):
    for j in range(c):
        if graph[i][j] != 'X':
            cur_water.append((i, j))
        if graph[i][j] == 'L':
            swan_x, swan_y = i, j

vis = [[False] * c for _ in range(r)]
cur_swan.append((swan_x, swan_y))
vis[swan_x][swan_y] = True
while not is_finished:

    find_swan()

    if not is_finished:
        find_melt()

        cur_water = copy.deepcopy(next_water)
        cur_swan = copy.deepcopy(next_swan)

        next_swan.clear()
        next_water.clear()
        res += 1

print(res)
