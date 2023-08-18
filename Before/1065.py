def han():
    n = 1000
    arr = []
    for i in range(1, n+1):
        if i < 100:
            arr.append(i)
        else:
            data = list(map(int, str(i)))
            if (data[1] * 2) == (data[0] + data[2]):
                arr.append(i)

    return arr


n = int(input())
data = han()
cnt = 0
for i in range(len(data)):
    if data[i] <= n:
        cnt += 1
print(cnt)
