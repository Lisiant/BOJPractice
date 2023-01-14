import sys

input = sys.stdin.readline


n, m = map(int, input().split())
j = int(input())
ns = [int(input()) for _ in range(j)]
min, max = 1, m
res = 0


for i in range(j):
    
    if ns[i] < min:
        res += min - ns[i]
        min = ns[i]
        max = min + m - 1
    elif ns[i] > max:
        res += ns[i] - max
        max = ns[i]
        min = max - m + 1
print(res)