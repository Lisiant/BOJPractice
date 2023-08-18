from collections import deque
import sys

n,m = map(int, sys.stdin.readline().split())
graph = []
result = 0

for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

visF = [[-1 for _ in range(m)] for _ in range(n)]
visJ = [[-1 for _ in range(m)] for _ in range(n)]

q1 = deque()
q2 = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'F':
            visF[i][j] = 0
            q1.append((i,j))
        
        elif graph[i][j] == 'J':
            visJ[i][j] = 0
            q2.append((i,j))


def bfsF(arr: list):
    x, y = q1.popleft()
    
    for i in range(4):    
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue

        if arr[nx][ny] >= 0 or graph[nx][ny] == '#': # 방문한 노드 혹은 벽
            continue
        
        arr[nx][ny] = arr[x][y] + 1
        q1.append((nx,ny))
    
    
def bfsJ(arr):
    
    while q2:
        x, y = q2.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                return arr[x][y] + 1
                 
            if (visF[nx][ny] <= visJ[x][y] + 1) and visF[nx][ny] != -1:
                continue
            
            if visJ[nx][ny] >= 0 or graph[nx][ny] == '#':
                continue
            
            
            visJ[nx][ny] = visJ[x][y] + 1
            q2.append((nx, ny))
    
    return -1
    
    
while q1:
    bfsF(visF)

result = bfsJ(visJ)

if result == -1:
    print("IMPOSSIBLE")
else:
    print(result)
    
    