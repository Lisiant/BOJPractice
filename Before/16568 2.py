import sys
input = lambda: sys.stdin.readline()
INF = int(1e9)

n, a, b = map(int, input().split())

d = [INF for _ in range(n + 1)]
d[0] = 0

for i in range(1, n + 1):
    d[i] = d[i - 1] + 1

    if i - a - 1 >= 0:
        d[i] = min(d[i], d[i - a - 1] + 1)

    if i - b - 1 >= 0:
        d[i] = min(d[i], d[i - b - 1] + 1)

print(d[n])
