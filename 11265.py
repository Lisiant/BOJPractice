import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a-1][b-1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")


"""다른 풀이(실행 속도 우수)"""
import sys
import heapq
input = sys.stdin.readline

def dijkstra2_2(s, e):
    INF = 1000000001
    distance = [INF] * (N + 1)

    heap = []
    heapq.heappush(heap, (0, s))
    distance[s] = 0

    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:  # 현재 노드가 처리된적 있다면 무시
            continue
        for next in range(1, N + 1):  # 현재 노드의 주변 노드를 탐색
            cost = dist + arr[now][next]
            if cost < distance[next]:  # 현재 노드를 거치는 것이 더 빠를 경우
                distance[next] = cost
                heapq.heappush(heap, (cost, next))

    record[s] = distance
    return distance[e]

N, M = map(int, input().split())
arr = [[]] + [[0] + list(map(int, input().split())) for _ in range(N)]

record = dict()
for _ in range(M):
    s, e, t = map(int, input().split())
    if record.get(s):
        if record[s][e] <= t:
            print('Enjoy other party')
        else:
            print('Stay here')
    else:
        if dijkstra2_2(s, e) <= t:
            print('Enjoy other party')
        else:
            print('Stay here')