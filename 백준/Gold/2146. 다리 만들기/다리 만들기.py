import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n


def fill_area(r, c, area):
    q = deque()
    q.append((r, c))
    labeled_graph[r][c] = area
    

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny, n):
                continue

            if graph[nx][ny] == 0:
                adj_zero_coordinates.append((nx, ny, area))
                continue

            if labeled_graph[nx][ny] != 0:
                continue

            labeled_graph[nx][ny] = area
            q.append((nx, ny))


def check_dist(r, c, area_num):
    global min_val

    q = deque()
    q.append((r, c))
    route = [[0] * n for _ in range(n)]
    route[r][c] = 1
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny, n):
                continue

            if labeled_graph[nx][ny] == area_num:
                continue

            if route[nx][ny] != 0:
                continue

            if labeled_graph[nx][ny] != 0:
                min_val = min(route[x][y], min_val)
                return

            route[nx][ny] = route[x][y] + 1
        
            q.append((nx, ny))


def print_arr(arr):
    for i in range(n):
        print(*arr[i])
    print()


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
labeled_graph = [[0] * n for _ in range(n)]
area_num = 1
min_val = INF

adj_zero_coordinates = []  # 상하좌우 중 하나가 0인 경우 -> (x좌표, y좌표, area_num)을 해당 배열에 append.

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and labeled_graph[i][j] == 0:
            fill_area(i, j, area_num)
            area_num += 1


for x, y, area_num in adj_zero_coordinates:
    check_dist(x, y, area_num)

print(min_val)
