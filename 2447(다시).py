'''
def drawStar(n):
    global data

    if n == 3:
        data[0][:3] = data[2][:3] = [1]*3
        data[1][:3] = [1, 0, 1]
        return

    a = n//3
    drawStar(n//3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                data[a*i+k][a*j:a*(j+1)] = data[k][:a]


n = int(input())
data = [[0 for i in range(n)] for j in range(n)]
drawStar(n)

for i in data:
    for j in i:
        if j:
            print("*", end='')
        else:
            print(" ", end='')
    print()
'''
'''

# 다른 풀이

from sys import setrecursionlimit
setrecursionlimit(10**6)


def drawStar(x, y, n):
    if n == 1:
        pan[x][y] = "*"
        return

    div = n//3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            drawStar(x+i*div, y+j*div, div)


n = int(input())
pan = [[' ' for _ in range(n)] for _ in range(n)]
drawStar(0, 0, n)
for i in range(n):
    print(''.join(pan[i]))
'''


# 혼자서 풀어보기

import sys
sys.setrecursionlimit(10**6)


def drawStar(x, y, n):
    global pan

    if n == 1:
        pan[x][y] = "*"
        return

    div = n // 3
    drawStar(x, y, div)
    drawStar(x, y+div, div)
    drawStar(x, y+div*2, div)
    drawStar(x+div, y, div)
    drawStar(x+div, y+div*2, div)
    drawStar(x+div*2, y, div)
    drawStar(x+div*2, y+div, div)
    drawStar(x+div*2, y+div*2, div)


n = int(sys.stdin.readline())
pan = [[' ' for _ in range(n)] for _ in range(n)]
drawStar(0, 0, n)

for i in range(n):
    for j in range(n):
        print(pan[i][j], end='')
    print()
