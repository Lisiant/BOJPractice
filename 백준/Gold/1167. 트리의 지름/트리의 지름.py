import sys
sys.setrecursionlimit(10**9)
input = lambda: sys.stdin.readline()

v = int(input())
tree = [[] for _ in range(v + 1)]
dist_root = [-1] * (v + 1)
dist = [-1] * (v + 1)

for i in range(v):
    data = list(map(int, input().split()))
    idx = 1

    while data[idx] != -1:
        tree[data[0]].append((data[idx], data[idx + 1]))
        idx += 2


def dfs(st, cur, arr):
    for node, edge in tree[st]:
        if arr[node] == -1:
            arr[node] = cur + edge
            dfs(node, cur + edge, arr)


dist_root[1] = 0
max_val = 0
left = 0
dfs(1, 0, dist_root)

for i in range(1, v + 1):
    if max_val < dist_root[i]:
        left = i
        max_val = dist_root[i]

dist[left] = 0
dfs(left, 0, dist)
print(max(dist))
