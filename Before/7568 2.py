n = int(input())
data = []
result = []

for i in range(n):
    x, y = map(int, input().split())
    data.append((x, y))

for i in data:
    rank = 1
    for j in data:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    result.append(rank)


for num in result:
    print(num, end=' ')
