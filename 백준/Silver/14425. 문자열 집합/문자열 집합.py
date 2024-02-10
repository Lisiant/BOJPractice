import sys

input = sys.stdin.readline

n, m = map(int, input().split())
res = 0
d = dict()
for i in range(n):
    x = input().rstrip()
    d[x] = 1

for i in range(m):
    if input().rstrip() in d:
        res += 1

print(res)