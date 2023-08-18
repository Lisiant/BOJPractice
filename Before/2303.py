import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
vals = []
res = 0
max_val = 0

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    combs = combinations(data, 3)
    val = 0

    for item in combs:
        val = max(val, sum(item) % 10)

    vals.append(val)


max_val = max(vals)
for i in range(len(vals) - 1, -1, -1):
    if vals[i] == max_val:
        print(i + 1)
        exit()
