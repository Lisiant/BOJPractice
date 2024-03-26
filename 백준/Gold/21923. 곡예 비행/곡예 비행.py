import sys
from collections import deque

input = lambda: sys.stdin.readline()
INF = -int(1e9)


def print_arr(arr):
    print()
    for i in range(n):
        print(*arr[i])


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
min_val, max_val = min(n, m), max(n, m)
rising = [[INF] * m for _ in range(n)]
descending = [[INF] * m for _ in range(n)]

rising[n - 1][0] = grid[n - 1][0]
descending[n - 1][0] = grid[n - 1][0]

for i in range(1, n):
    rising[n - i - 1][0] = rising[n - i][0] + grid[n - i - 1][0]

for i in range(1, m):
    rising[n - 1][i] = rising[n - 1][i - 1] + grid[n - 1][i]

for i in range(1, n):
    for j in range(1, m):
        rising[n - i - 1][j] = max(rising[n - i - 1][j - 1] + grid[n - i - 1][j],
                                   rising[n - i][j] + grid[n - i - 1][j])

descending[n - 1][m - 1] = grid[n - 1][m - 1]
# descending[i][j] = i,j에서 도착지까지 하강비행했을 때 비용 = 도착지에서 i,j까지 상승비행(왼쪽,위)
for i in range(1, m):
    descending[n - 1][m - i - 1] = descending[n - 1][m - i] + grid[n - 1][m - i - 1]

for i in range(1, n):
    descending[n - i - 1][m - 1] = descending[n - i][m - 1] + grid[n - 1 - i][m - 1]

for i in range(1, n):
    for j in range(1, m):
        descending[n - i - 1][m - j - 1] = max(descending[n - i][m - j - 1] + grid[n - i - 1][m - j - 1],
                                               descending[n - i - 1][m - j] + grid[n - i - 1][m - j - 1])

res = INF
for i in range(n):
    for j in range(m):
        res = max(res, rising[i][j] + descending[i][j])

print(res)
