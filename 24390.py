import sys
input = sys.stdin.readline
INF = int(1e9)

res = [INF] * 3601
arr = [10, 60, 600]


m, s = map(int, input().split(':'))
time = 60 * m + s
res[0] = 1
res[10], res[20] = 2, 3
res[30] = 1


for i in range(3601):
    for j in range(3):
        if i - arr[j] >= 0:
            res[i] = min(res[i], res[i - arr[j]] + 1)

print(res[time])
