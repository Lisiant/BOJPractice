import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, k):
    res = 0
    dist = 0
    q = deque()

    q.append((start, 0))

    while q:
        cur, dist = q.popleft()
        if dist <= k and apples[cur] == 1:
            res += 1

        for child in graph[cur]:
            q.append((child, dist+1))
    
    return res
            
            
n, k = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(n-1):
    p, c = map(int, input().split())
    graph[p].append(c)

apples = list(map(int, input().split()))

print(bfs(0, k))