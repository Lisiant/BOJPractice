import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
temp = [0] * 1000001
cnt = 0


for i in range(n):
    if temp[x - data[i]]:
        cnt += 1
    else:
        temp[data[i]] = 1

print(cnt)
