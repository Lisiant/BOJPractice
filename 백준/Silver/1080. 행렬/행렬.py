import sys

input = lambda: sys.stdin.readline()

n, m = map(int, input().split())
A = [list(map(int, input().rstrip())) for _ in range(n)]
B = [list(map(int, input().rstrip())) for _ in range(n)]
cnt = 0

def flip(x, y):
    global cnt

    for i in range(3):
        for j in range(3):
            A[x + i][y + j] = 1 if A[x + i][y + j] == 0 else 0

    cnt += 1


for i in range(n - 2):
    for j in range(m - 2):
        if A[i][j] != B[i][j]:
            flip(i, j)

for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            print(-1)
            exit()
print(cnt)
