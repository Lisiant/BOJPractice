import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
data = list(map(int, input().split()))
res = []
idx = 0
flag = True


for i in range(0, n, 2):
    res.append((data[i], data[i+1], data[i+1] - data[i]))

for temp in res:
    if temp[0] < temp[1]:
        idx = max(idx, temp[2])

for temp in res:
    if temp[0] < temp[1]:
        if flag:
            if idx == temp[2]:
                cnt += temp[1]
                flag = False
        else:
            cnt += temp[0]
    else:
        cnt += temp[0]
print(cnt)