import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
old = [list(map(int, input().split())) for _ in range(n)]


def rotate_all_once(old):
    new = [[0] * m for _ in range(n)]
    layer_num = min(n, m) // 2

    for i in range(layer_num):
        rotate_layer(old, new, i)

    # print_arr(old, n, m)
    # print()
    # print_arr(new, n, m)

    return new


def rotate_layer(old, new, l):
    for i in range(l + 1, m - l):
        new[l][i - 1] = old[l][i]
        new[n - 1 - l][i] = old[n - 1 - l][i - 1]

    for i in range(l + 1, n - l):
        new[i][l] = old[i - 1][l]
        new[i - 1][m - 1 - l] = old[i][m - 1 - l]


def print_arr(arr, row, col):
    for i in range(row):
        for j in range(col):
            print(arr[i][j], end=' ')
        print()


def solution(rotate_num, arr):
    temp = arr
    while rotate_num > 0:
        temp = rotate_all_once(temp)
        rotate_num -= 1
    return temp


res = solution(r, old)
print_arr(res, n, m)
