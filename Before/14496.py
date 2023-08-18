import sys
import heapq
from types import new_class
INF = int(1e9)
input = sys.stdin.readline

a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [INF for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append((1, y))
    graph[y].append((1, x))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        cur_cost, cur_node = heapq.heappop(q)

        if cur_cost > dist[cur_node]:
            continue

        for next_node_info in graph[cur_node]:
            cost = cur_cost + next_node_info[0]

            if cost < dist[next_node_info[1]]:
                dist[next_node_info[1]] = cost
                heapq.heappush(q, (cost, next_node_info[1]))


dijkstra(a)
res = dist[b]

if res != INF:
    print(res)
else:
    print(-1)
