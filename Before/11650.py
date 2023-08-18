import sys

tc = int(sys.stdin.readline())
data = []
for i in range(tc):
    x, y = map(int, sys.stdin.readline().split())
    data.append((x, y))


data.sort(key=lambda x: (x[0], x[1]))

for x, y in data:
    print(x, y)
