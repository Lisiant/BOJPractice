import sys

input = lambda: sys.stdin.readline()
INF = int(1e9)

t = int(input())


def next_permutation(arr, n):
    idx = n - 1
    while idx > 0 and arr[idx - 1] >= arr[idx]:
        idx -= 1

    pivot = idx - 1 if idx > 0 else 0
    pivot_val = arr[pivot]
    swap_val = INF
    swap_idx = 0
    for i in range(pivot + 1, n):
        if arr[i] > pivot_val:
            if arr[i] <= swap_val:
                swap_val = arr[i]
                swap_idx = i

    if pivot == 0 and swap_idx == 0:
        return ''.join(map(str, arr))

    arr[pivot] = swap_val
    arr[swap_idx] = pivot_val
    result = arr[:pivot + 1] + arr[pivot + 1:][::-1]

    return ''.join(map(str, result))


for _ in range(t):
    data = list(map(int, input().rstrip()))
    val = ''.join(map(str, data))
    n = len(data)
    res = next_permutation(data, n)

    if res == val:
        print("BIGGEST")
    else:
        print(res)
