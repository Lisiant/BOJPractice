import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, dist):
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


tc = int(input())
for _ in range(tc):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    distance_start = [INF for _ in range(n+1)]
    distance_g = [INF for _ in range(n+1)]
    distance_h = [INF for _ in range(n+1)]

    candidate = []
    result = []
    waypoint_distance = 0

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

        if (a == g and b == h) or (a == h and b == g):
            waypoint_distance = d

    for _ in range(t):
        x = int(input())
        candidate.append(x)

    dijkstra(s, distance_start)
    dijkstra(g, distance_g)
    dijkstra(h, distance_h)

    for i in range(t):
        check = distance_start[candidate[i]]

        temp1 = distance_g[candidate[i]] + \
            waypoint_distance + distance_start[h]

        temp2 = distance_h[candidate[i]] + \
            waypoint_distance + distance_start[g]

        if check == temp1 or check == temp2:
            result.append(candidate[i])

    result.sort()
    print(*result)
