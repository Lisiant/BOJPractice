import sys
from itertools import combinations

input = lambda: sys.stdin.readline()

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
lst = [i for i in range(0, n)]
res = int(1e9)


def get_right(left):
    right = []
    for i in range(n):
        if i not in left:
            right.append(i)
    return right


def calc_val(arr):
    temp = 0
    comb = combinations(arr, 2)
    for i, j in comb:
        temp += (data[i][j] + data[j][i])

    return temp


for item in list(combinations(lst, n // 2)):
    left = list(item)
    right = get_right(left)

    res = min(res, abs(calc_val(left) - calc_val(right)))
print(res)