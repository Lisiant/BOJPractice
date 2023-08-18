def d(n):
    res = n + sum(map(int, str(n)))
    return res


n = 10000
data = [0] * (n+1)
for i in range(1, n):
    if d(i) <= n:
        data[d(i)] = 1

for i in range(1, n):
    if data[i] == 0:
        print(i)
