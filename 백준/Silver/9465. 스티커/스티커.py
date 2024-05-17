import sys

input = lambda: sys.stdin.readline()

t = int(input())
for _ in range(t):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    if n == 1:
        print(max(grid[0][0], grid[1][0]))
        continue

    dp[0][0] = grid[0][0]
    dp[1][0] = grid[1][0]
    dp[0][1] = grid[0][1] + dp[1][0]
    dp[1][1] = grid[1][1] + dp[0][0]

    for i in range(2, n):
        dp[0][i] = max(dp[0][i - 2], dp[1][i - 2], dp[1][i - 1]) + grid[0][i]
        dp[1][i] = max(dp[1][i - 2], dp[0][i - 2], dp[0][i - 1]) + grid[1][i]

    print(max(dp[0][n - 1], dp[1][n - 1]))
