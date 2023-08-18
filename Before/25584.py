import sys
input = lambda: sys.stdin.readline()

INF = int(1e9)

n = int(input())
res = dict()

for i in range(n):
    data = []
    for j in range(4):
        data.append(list(map(str, input().split())))

    for j in range(4):
        for k in range(7):
            if data[j][k] == '-':
                continue

            if data[j][k] in res:
                if j == 0:
                    res[data[j][k]] += 4
                elif j == 1:
                    res[data[j][k]] += 6
                elif j == 2:
                    res[data[j][k]] += 4
                else:
                    res[data[j][k]] += 10

            else:
                if j == 0:
                    res[data[j][k]] = 4
                elif j == 1:
                    res[data[j][k]] = 6
                elif j == 2:
                    res[data[j][k]] = 4
                else:
                    res[data[j][k]] = 10



max_val, min_val = 0, INF
for key in res:
    if res[key] > max_val:
        max_val = res[key]
        
    if res[key] < min_val:
        min_val = res[key]

if max_val - min_val > 12:
    print('No')
else:
    print('Yes')