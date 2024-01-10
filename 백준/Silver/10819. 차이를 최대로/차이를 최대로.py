import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

max_val = -1000

n = int(input())
data = list(map(int, input().split()))
is_used = [False] * n
temp = [0] * n


def calc(arr):
    res = 0
    for i in range(n - 1):
        res += abs(arr[i] - arr[i + 1])
    return res


def solve(idx):
    global max_val

    if idx == n:
        max_val = max(max_val, calc(temp))
        return

    for i in range(n):
        if not is_used[i]:
            is_used[i] = True
            temp[idx] = data[i]
            solve(idx + 1)
            is_used[i] = False


solve(0)
print(max_val)
