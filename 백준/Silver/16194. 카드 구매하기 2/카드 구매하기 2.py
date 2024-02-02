import sys

input = lambda: sys.stdin.readline()

n = int(input())
prices = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
dp[0] = prices[0]
dp[1] = prices[1]

for i in range(2, n+1):
    dp[i] = prices[i]
    for j in range(i):
        dp[i] = min(dp[i], dp[i-j] + prices[j])

print(dp[n])
