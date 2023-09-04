import sys

MAX_VAL = int(1e9) + 1

input = sys.stdin.readline

res = []
n = int(input())
data = list(map(int, input().split()))
plus = []
minus = []

for item in data:
    if item < 0:
        minus.append(-item)
    else:
        plus.append(item)

plus.sort()
minus.sort()

if len(plus) == 0:
    print(-minus[1], -minus[0])
    exit(0)
elif len(minus) == 0:
    print(plus[0], plus[1])
    exit(0)


def binary_search(target, arr):
    st, en = 0, len(arr)

    while st < en:
        mid = (st + en) // 2

        if arr[mid] >= target:
            en = mid
        else:
            st = mid + 1

    return st

temp_diff = MAX_VAL
temp_idx = 0
for x in plus:
    idx = binary_search(x, minus)

    if idx == 0:
        diff = abs(x - minus[0])
        temp_idx = idx
    elif idx == len(minus):
        diff = abs(x - minus[idx - 1])
        temp_idx = idx - 1
    else:
        diff1 = abs(x - minus[idx])
        diff2 = abs(x - minus[idx - 1])
        if diff1 <= diff2:
            diff = diff1
            temp_idx = idx
        else:
            diff = diff2
            temp_idx = idx - 1

    if temp_diff > diff:
        temp_diff = diff
        res = [x, -minus[temp_idx]]

if len(plus) > 1 and temp_diff > abs(plus[0] + plus[1]):
    res = [plus[0], plus[1]]


print(*sorted(res))

