import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
depths = [0] * (n + 1)
vis = [False] * (n + 1)
is_leaf = [True] * (n + 1)


for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def calc_depth(root):
    q = deque()
    q.append(root)
    vis[root] = True

    while q:
        cur = q.popleft()

        for nn in tree[cur]:
            if vis[nn]:
                continue

            is_leaf[cur] = False
            vis[nn] = True
            depths[nn] = depths[cur] + 1
            q.append(nn)


def is_sw_wins():
    res = 0
    for i in range(1, n + 1):
        if is_leaf[i]:
            res += depths[i]

    return res % 2 != 0


calc_depth(1)
print("Yes") if is_sw_wins() else print("No")
