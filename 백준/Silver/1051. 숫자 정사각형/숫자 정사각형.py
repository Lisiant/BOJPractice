import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = []
res = 1
for _ in range(n):
    data.append(list(map(int, input().rstrip())))

min_val = min(n, m)
if min_val < 2:
    print(1)
    exit()


def check(n, m, t):
    for i in range(n - t):
        for j in range(m - t):
            if data[i][j] == data[i][j + t] and data[i][j] == data[i + t][j + t] and data[i][j] == data[i + t][j]:
                return True
    return False


for t in range(1, min_val):
    if check(n, m, t):
        res = t + 1

print(res ** 2)
