import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):

    for i in range(n+1):
        dist[i] = INF

    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:

        cur_dist, cur_node = heapq.heappop(q)
        if cur_dist > dist[cur_node]:
            continue

        for next_node_info in graph[cur_node]:
            next_dist = cur_dist + next_node_info[1]

            if next_dist < dist[next_node_info[0]]:
                dist[next_node_info[0]] = next_dist
                heapq.heappush(q, (next_dist, next_node_info[0]))


n, m, r = map(int, input().split())
item = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
dist = [INF for _ in range(n+1)]
res = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))


for i in range(1, n+1):
    dijkstra(i)
    temp = 0

    for j in range(1, n+1):
        if dist[j] <= m:
            temp += item[j]

    res = max(res, temp)

print(res)
