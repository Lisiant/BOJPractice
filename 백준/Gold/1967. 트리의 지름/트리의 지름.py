import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(st, cur, vis):
    for node, edge in tree[st]:
        if vis[node] == -1:
            vis[node] = cur + edge
            dfs(node, cur + edge, vis)


n = int(input())
tree = [[] for _ in range(n + 1)]
dist_from_root = [-1] * (n + 1)
dist = [-1] * (n + 1)
left = [0, 0]

for i in range(n - 1):
    parent, child, edge = map(int, input().split())
    tree[parent].append((child, edge))
    tree[child].append((parent, edge))

dist_from_root[1] = 0
dfs(1, 0, dist_from_root)

for i in range(1, n + 1):
    if left[0] < dist_from_root[i]:
        left[0] = dist_from_root[i]
        left[1] = i

dist[left[1]] = 0
dfs(left[1], 0, dist)

print(max(dist))