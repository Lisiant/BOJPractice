import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

INF = int(1e10)

max_val, min_val = 0, INF
max_str, min_str = "", ""
n = int(input())
data = list(input().split())
isused = [False] * 10
temp = [0] * 10


def is_valid(arr, idx):
    for i in range(idx):
        if data[i] == "<":
            if arr[i] > arr[i + 1]:
                return False

        elif data[i] == ">":
            if arr[i] < arr[i + 1]:
                return False

    return True


def arr_to_str(arr):
    return "".join(map(str, arr))


def is_max_val(val):
    return max_val < val


def is_min_val(val):
    return min_val > val


def set_max_val(val):
    global max_str, max_val
    int_val = int(val)
    if is_max_val(int_val):
        max_val = int_val
        max_str = val


def set_min_val(val):
    global min_str, min_val
    int_val = int(val)
    if is_min_val(int(val)):
        min_val = int_val
        min_str = val


def solve(idx):
    global max_val, min_val

    if idx == n + 1:
        res = []
        for i in range(n + 1):
            res.append(temp[i])

        val = arr_to_str(res)
        set_max_val(val)
        set_min_val(val)

        return

    for i in range(10):
        if not isused[i]:
            isused[i] = True
            temp[idx] = i
            if is_valid(temp, idx):
                solve(idx + 1)
            isused[i] = False


solve(0)
print(max_str)
print(min_str)
