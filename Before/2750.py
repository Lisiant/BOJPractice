import sys
tc = int(sys.stdin.readline())

data = []
for i in range(tc):
    n = int(sys.stdin.readline())
    data.append(n)

data.sort()

for i in data:
    print(i)
