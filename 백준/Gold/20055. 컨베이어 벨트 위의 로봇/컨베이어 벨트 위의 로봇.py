import sys
from collections import deque

input = lambda: sys.stdin.readline()

n, k = map(int, input().split())
data = deque((map(int, input().split())))
belt = deque([0] * (n * 2))
res = 1


def rotate():
    data.appendleft(data.pop())
    belt.appendleft(belt.pop())
    unload()


def is_movable(i):
    return data[i] > 0 and belt[i] != 1


def move_robot(idx):
    i = (idx + 1) % (n * 2)

    if is_movable(i):
        data[i] -= 1
        belt[idx] = 0
        belt[i] = 1

    unload()


def lift():
    if data[0] > 0:
        data[0] -= 1
        belt[0] = 1


def unload():
    if belt[n - 1] == 1:
        belt[n - 1] = 0


def check():
    cnt = 0

    for i in range(2 * n):
        if data[i] <= 0:
            cnt += 1

    if cnt >= k:
        return True

    return False


def simulate():
    global res

    while True:

        rotate()
        for i in range(2 * n - 1, -1, -1):
            if belt[i] == 1:
                move_robot(i)

        lift()
        if check():
            return res
        res += 1


print(simulate())
