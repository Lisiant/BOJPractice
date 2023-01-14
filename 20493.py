import sys
input = sys.stdin.readline

n, t = map(int, input().split())
x, y = 0, 0
flag = 0
cur = 0

for _ in range(n):
    time, direction = input().split()
    distance = int(time) - cur
    cur = int(time)

    if direction == 'right':
        if flag == 0:           # 현재 오른쪽으로 진행
            x += distance
            flag = 1
        elif flag == 1:         # 현재 아래
            y -= distance
            flag = 3
        elif flag == 2:         # 현재 위
            y += distance
            flag = 0
        elif flag == 3:         # 현재 왼쪽
            x -= distance
            flag = 2
    else:
        if flag == 0:
            x += distance
            flag = 2

        elif flag == 1:
            y -= distance
            flag = 0
        elif flag == 2:
            y += distance
            flag = 3
        elif flag == 3:
            x -= distance
            flag = 1


distance = t - cur
if flag == 0:
    x += distance
elif flag == 1:
    y -= distance
elif flag == 2:
    y += distance
elif flag == 3:
    x -= distance


print(x, y)
