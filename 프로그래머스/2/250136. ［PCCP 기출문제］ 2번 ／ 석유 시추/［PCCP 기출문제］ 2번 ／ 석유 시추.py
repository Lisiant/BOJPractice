from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

vis = [[0] * 500 for _ in range(500)]
n = 0
m = 0

def bfs(a, b, vis, land, cnt):
    global n, m
    q = deque()
    vis[a][b] = cnt
    q.append((a, b))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if not in_range(nx, ny):
                continue
            
            if vis[nx][ny] or land[nx][ny] == 0:
                continue
            
            vis[nx][ny] = cnt
            q.append((nx, ny))
    


def in_range(x, y):
    global n, m
    return 0 <= x < n and 0 <= y < m
    
    
def solution(land):
    global n, m
    answer = 0
    
    n = len(land)
    m = len(land[0])
    
    cnt = 1
    area = [0] * 130000
    
    
    
    for i in range(n):
        for j in range(m):
            
            if land[i][j] != 0 and vis[i][j] == 0:
                bfs(i, j, vis, land, cnt)
                cnt += 1
                
                
    
    for i in range(n):
        for j in range(m):
            num = vis[i][j]
            if num != 0:
                area[num] += 1
                    
                    
                    
    for i in range(m):
        oils = set()
        temp = 0
        for j in range(n):
            if vis[j][i] != 0:
                oils.add(vis[j][i])
                
        for num in oils:
            temp += area[num]
        
        answer = max(answer,temp)
        

    return answer