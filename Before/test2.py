from collections import deque
import sys

n,m,k,x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)] # graph의 n번째 요소(리스트)는 n번째 도시를 의미
vis = [-1 for i in range(n+1)] # 방문 여부를 나타내는 리스트
for _ in range(m):
    a, b= map(int, sys.stdin.readline().split())
    graph[a].append(b) # a 도시는 b 도시와 연결되어 있음을 표시
    

queue = deque()
queue.append(x)

vis[x] = 0

while queue:
    now = queue.popleft()
    for next_node in graph[now]:
        if vis[next_node] >= 0:
            continue
        if vis[next_node] == -1: # 아직 방문하지 않은 노드라면
            
            vis[next_node] = vis[now] + 1
            queue.append(next_node)


non_exist = True
for i in range(len(vis)):
    if vis[i] == k:
        print(i)
        non_exist = False
        
if non_exist:
    print(-1)
    
            
    
