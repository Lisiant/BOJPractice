import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:

        cur_dist, cur_node = heapq.heappop(q)
        if cur_dist > dist[cur_node]:
            continue

        for next_node_info in graph[cur_node]:
            cost = cur_dist + next_node_info[1]

            if cost < dist[next_node_info[0]]:
                dist[next_node_info[0]] = cost
                heapq.heappush(q, (cost, next_node_info[0]))


tc = int(input())
for _ in range(tc):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    dist = [INF for _ in range(n+1)]
    com, time = 0, 0

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    dijkstra(c)
    for i in range(1, n+1):
        if dist[i] != INF:
            com += 1
            time = max(time, dist[i])

    print(com, time)
