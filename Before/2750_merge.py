import sys
input = sys.stdin.readline

n = int(input())
arr = []
res = [0] * 1000001

for _ in range(n):
    arr.append(int(input()))


def merge(st: int, en: int):
    mid = (st+en) // 2
    lidx = st
    ridx = mid

    for i in range(st, en):
        if ridx == en:
            res[i] = arr[lidx]
            lidx += 1

        elif lidx == mid:
            res[i] = arr[ridx]
            ridx += 1

        elif arr[lidx] <= arr[ridx]:
            res[i] = arr[lidx]
            lidx += 1

        else:
            res[i] = arr[ridx]
            ridx += 1

    for i in range(st, en):
        arr[i] = res[i]


def merge_sort(st: int, en: int):
    if st + 1 == en:
        return

    mid = (st+en) // 2
    merge_sort(st, mid)
    merge_sort(mid, en)
    merge(st, en)


merge_sort(0, n)
for i in range(n):
    print(arr[i])
