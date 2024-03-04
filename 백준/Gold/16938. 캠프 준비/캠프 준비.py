import sys
from itertools import combinations

input = sys.stdin.readline

n, l, r, x = map(int, input().split())
data = list(map(int, input().split()))
res = 0


def is_valid(combination):
    if l <= sum(combination) <= r and max(combination) - min(combination) >= x:
        return True
    return False


for i in range(1, n + 1):
    for combination in combinations(data, i):
        if is_valid(combination):
            res += 1
print(res)