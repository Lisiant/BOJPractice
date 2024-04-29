import sys

input = sys.stdin.readline

n, d = map(int, input().split())
dp = [i for i in range(d + 1)]

dist = []

for _ in range(n):
    dist.append(list(map(int, input().split())))

dist.sort()

for i in range(d + 1):
    dp[i] = min(dp[i], dp[i-1]+1)

    for st, en, distance in dist:
        if i == st:
            if en <= d:
                dp[en] = min(dp[i] + distance, dp[en])

print(dp[d])
