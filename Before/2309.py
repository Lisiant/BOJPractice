data = [int(input()) for _ in range(9)]
temp = sum(data) - 100

for i in range(8):
    for j in range(i+1, 9):
        if data[i] + data[j] == temp:
            a = data[i]
            b = data[j]
            break

data.remove(a)
data.remove(b)

for i in sorted(data):
    print(i)
