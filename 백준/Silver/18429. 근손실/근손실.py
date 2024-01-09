import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
LIMIT = 500

n, k = map(int, input().split())
data = list(map(int, input().split()))
is_used = [False] * len(data)

res = 0


def check(val):
    return val >= LIMIT


def solve(idx, cur):
    global res
    if idx == n:
        res += 1
        return

    for i in range(n):
        if not is_used[i]:
            is_used[i] = True
            new_val = cur - k + data[i]
            if check(new_val):
                solve(idx + 1, new_val)
            is_used[i] = False


solve(0, LIMIT)
print(res)
