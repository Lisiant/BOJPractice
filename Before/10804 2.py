data = [i for i in range(1, 21)]
for _ in range(10):
    a, b = map(int, input().split())

    for i in range(a-1, (a+b)//2):
        temp = data[i]
        data[i] = data[((a-1)+(b-1))-i]
        data[((a-1)+(b-1))-i] = temp

for i in data:
    print(i, end=' ')
