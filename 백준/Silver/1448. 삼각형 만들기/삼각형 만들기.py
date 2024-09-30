import sys

input = lambda: sys.stdin.readline()

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort(reverse=True)
res = -1
for i in range(n - 2):
    a, b, c = data[i], data[i+1], data[i+2]
    if a < b + c:
        res = a+b+c
        break

print(res)

