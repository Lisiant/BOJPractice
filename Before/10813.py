import sys

n, m = map(int, sys.stdin.readline().split())
graph = [i for i in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a], graph[b] = graph[b], graph[a]

print(*graph[1:])