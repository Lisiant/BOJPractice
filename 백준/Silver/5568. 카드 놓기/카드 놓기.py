import sys
from collections import defaultdict

input = lambda: sys.stdin.readline()
n = int(input())
k = int(input())
nums = [int(input()) for _ in range(n)]
vis = [False] * n
d = defaultdict()
temp = [0] * k


def solve(idx):
    global temp

    if idx == k:
        d[''.join(list(map(str, temp)))] = 0
        return

    for i in range(n):
        if not vis[i]:
            vis[i] = True
            temp[idx] = nums[i]
            solve(idx + 1)
            vis[i] = False


solve(0)
print(len(d.keys()))
