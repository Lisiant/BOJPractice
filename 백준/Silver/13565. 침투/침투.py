import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
vis = [[False] * m for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.pop()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not in_range(nx, ny) or graph[nx][ny] == 1 or vis[nx][ny]:
                continue
            
            vis[nx][ny] = True
            q.append((nx, ny))

def is_valid(arr):
    
    for i in range(m):
        if arr[n-1][i]:
            return True
    
    return False


for i in range(m):
    if graph[0][i] == 0:
        bfs(0, i)
    
print("YES") if is_valid(vis) else print("NO")