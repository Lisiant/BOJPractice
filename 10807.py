import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())
cnt = 0


for num in data:
    if v == num:
        cnt += 1

print(cnt)
