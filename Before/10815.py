import sys


def binary_search(array, target, start, end):
    while start <= end:

        mid = (start + end) // 2

        if array[mid] == target:
            return True

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return False


n = int(sys.stdin.readline())
sg = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
res = []

for i in range(m):
    start = 0
    end = n-1
    temp = binary_search(sg, data[i], start, end)

    if temp:
        res.append(1)
    else:
        res.append(0)

for j in range(m):
    print(res[j], end=' ')
