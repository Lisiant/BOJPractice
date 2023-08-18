import sys
input = sys.stdin.readline
INF = 10
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n = int(input())
mine = [list(map(str, input().rstrip())) for _ in range(n)]
status = [list(map(str, input().rstrip())) for _ in range(n)]
cnt = [[0] * n for _ in range(n)]


def check_mine(x, y):

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= n or ny >= n or nx < 0 or ny < 0:
            continue

        if mine[nx][ny] == '*':
            cnt[x][y] += 1


def check_unpacked(arr):
    flag = False

    for i in range(n):
        for j in range(n):
            if status[i][j] == '.':
                arr[i][j] = '.'
            else:  # 열린 칸에 대해서
                if mine[i][j] == '*':  # 지뢰를 밟은 경우
                    arr[i][j] = '*'
                    flag = True

    return flag


def print_mine(arr):
    for i in range(n):
        for j in range(n):
            if mine[i][j] == '*':
                arr[i][j] = '*'


for i in range(n):
    for j in range(n):
        check_mine(i, j)

if check_unpacked(cnt):
    print_mine(cnt)

for i in range(n):
    for j in range(n):
        print(cnt[i][j], end='')
    print()
