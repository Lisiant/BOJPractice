import sys, copy

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
res = 0
dirs = [0] * 5


def move_up(temp):
    for i in range(n):
        pivot = 0

        for j in range(1, n):
            if temp[j][i] == 0:
                continue

            cur = temp[j][i]
            temp[j][i] = 0

            if temp[pivot][i] == 0:
                temp[pivot][i] = cur

            elif temp[pivot][i] == cur:
                temp[pivot][i] *= 2
                pivot += 1

            else:
                pivot += 1
                temp[pivot][i] = cur


def move_down(temp):
    for i in range(n):
        pivot = n - 1

        for j in range(n - 2, -1, -1):
            if temp[j][i] == 0:
                continue

            cur = temp[j][i]
            temp[j][i] = 0

            if temp[pivot][i] == 0:
                temp[pivot][i] = cur

            elif temp[pivot][i] == cur:
                temp[pivot][i] *= 2
                pivot -= 1

            else:
                pivot -= 1
                temp[pivot][i] = cur


def move_left(temp):
    for i in range(n):
        pivot = 0

        for j in range(1, n):
            if temp[i][j] == 0:
                continue

            cur = temp[i][j]
            temp[i][j] = 0

            if temp[i][pivot] == 0:
                temp[i][pivot] = cur

            elif temp[i][pivot] == cur:
                temp[i][pivot] *= 2
                pivot += 1

            else:
                pivot += 1
                temp[i][pivot] = cur


def move_right(temp):
    for i in range(n):
        pivot = n - 1

        for j in range(n - 2, -1, -1):
            if temp[i][j] == 0:
                continue

            cur = temp[i][j]
            temp[i][j] = 0

            if temp[i][pivot] == 0:
                temp[i][pivot] = cur

            elif temp[i][pivot] == cur:
                temp[i][pivot] *= 2
                pivot -= 1

            else:
                pivot -= 1
                temp[i][pivot] = cur


def move(dirs):
    temp = copy.deepcopy(graph)

    for dir in dirs:
        if dir == 0:
            move_up(temp)
        elif dir == 1:
            move_down(temp)
        elif dir == 2:
            move_left(temp)
        else:
            move_right(temp)

    return calc_max_val(temp)


def solve(idx):
    global res

    if idx == 5:
        res = max(res, move(dirs))
        return

    for i in range(4):
        dirs[idx] = i
        solve(idx + 1)


def calc_max_val(arr):
    max_val = 0

    for i in range(n):
        for j in range(n):
            max_val = max(max_val, arr[i][j])
    return max_val


solve(0)
print(res)