from collections import deque
import sys

r, c = map(int, sys.stdin.readline().split())
maze = []
for i in range(r):
    maze.append(list(sys.stdin.readline().rstrip()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visF = [[-1 for _ in range(c)] for _ in range(r)]
visJ = [[-1 for _ in range(c)] for _ in range(r)]

q1 = deque()
q2 = deque()

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'F':
            q1.append((i,j))
            visF[i][j] = 0
        
        if maze[i][j] == 'J':
            q2.append((i,j))
            visJ[i][j] = 0
        
        
while q1:
    x, y = q1.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= r or nx < 0 or ny >= c or ny < 0:
            continue
    
        if visF[nx][ny] >= 0 or maze[nx][ny] == '#':
            continue
        
        visF[nx][ny] = visF[x][y] + 1
        q1.append((nx,ny))

while q2:
    x, y = q2.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= r or nx < 0 or ny >= c or ny < 0:  # 탈출에 성공했을 때 출력해야 하는 값은 최초로 탈출한 시간.
            print(visJ[x][y] + 1) # visJ[x][y] == 탈출하기 직전의 거리 ->  탈출한 시간을 구해야 하므로 +1 해서 출력.          
            exit() # 답을 출력하고 종료
            
        if (visF[nx][ny] <= visJ[x][y] + 1) and visF[nx][ny] != -1: # 불의 전파 시간을 조건에 추가
            continue
        
        if visJ[nx][ny] >= 0 or maze[nx][ny] == '#':
            continue
            
        visJ[nx][ny] = visJ[x][y] + 1
        q2.append((nx,ny))
        
print("IMPOSSIBLE") # 프로그램이 종료되지 않고 여기에 도달했다는 것은 탈출에 실패함을 의미.
