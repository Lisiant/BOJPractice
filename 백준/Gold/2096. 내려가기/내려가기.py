import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
min_grid = [0, 0, 0]
max_grid = [0, 0, 0]

for i in range(n):
    input_grid = list(map(int, input().split()))

    a, b, c = (min(min_grid[0], min_grid[1]) + input_grid[0],
               min(min_grid) + input_grid[1],
               min(min_grid[1], min_grid[2]) + input_grid[2])
    min_grid[0], min_grid[1], min_grid[2] = a, b, c
    
    a, b, c = (max(max_grid[0], max_grid[1]) + input_grid[0],
               max(max_grid) + input_grid[1],
               max(max_grid[1], max_grid[2]) + input_grid[2])
    max_grid[0], max_grid[1], max_grid[2] = a, b, c


print(max(max_grid), min(min_grid))
