import sys
from collections import deque

input = sys.stdin.readline

data = [deque()]

# key: value -> key번 톱니바퀴를 돌릴지 말 지 여부. 1이면 시계, 0이면 pass, -1이면 반시계
dic = {
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

for i in range(4):
    info = list(input().rstrip())
    data.append(deque(list(map(int, info))))

k = int(input())


# num - 1과 num을 비교하여 dic[num]을 변경하고 check_ascend(num+1)을 호출
def check_ascend(num):
    if num == 5:
        return

    # 다른 극인 경우
    if data[num - 1][2] != data[num][6]:
        if dic[num - 1] == -1:
            dic[num] = 1
        elif dic[num - 1] == 1:
            dic[num] = -1

    check_ascend(num + 1)


# num + 1과 num을 비교하여 dic[num]을 변경하고 check_descend(num-1)을 호출
def check_descend(num):
    if num == 0:
        return

    if data[num + 1][6] != data[num][2]:
        if dic[num + 1] == -1:
            dic[num] = 1
        elif dic[num + 1] == 1:
            dic[num] = -1

    check_descend(num - 1)


def solve(num, direction):
    dic[num] = direction

    check_ascend(num + 1)
    check_descend(num - 1)

    for item in dic.keys():
        if dic[item] == 1:
            rotate_clockwise(item)
        elif dic[item] == -1:
            rotate_counterclockwise(item)

        dic[item] = 0

    # print(data[1:])


def rotate_counterclockwise(num):
    data[num].append(data[num].popleft())


def rotate_clockwise(num):
    data[num].appendleft(data[num].pop())


def calc_score():
    res = 0

    for i in range(4):
        if data[i + 1][0] == 1:
            res += (2 ** i)
    return res


for _ in range(k):
    a, b = map(int, input().split())
    solve(a, b)

print(calc_score())
