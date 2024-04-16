import sys

input = lambda: sys.stdin.readline()
n = int(input())

if n == 0:
    print(0)
    exit()

data = [int(input()) for _ in range(n)]
data.sort()

boundary = round(n * 0.15 + 0.000001)
res = sum(data[boundary:n - boundary]) / (n - 2 * boundary)
print(round(res + 0.000001))