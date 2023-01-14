n = int(input())

data = []
for i in range(n):
    x, y = map(int, input().split())
    data.append((x, y))
data.sort(key=lambda x: (x[1], x[0]))


for x, y in data:
    print(x, y)
