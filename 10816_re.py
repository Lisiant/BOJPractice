import sys


def lower_bound(array, target):
    start = 0
    end = len(array)

    while start < end:
        mid = (start + end) // 2

        if array[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start

    
def upper_bound(array, target):
    start = 0
    end = len(array)
    while start < end:

        mid = (start + end) // 2
        if array[mid] <= target:
            start = mid + 1
        else:
            end = mid

    return start


n = int(sys.stdin.readline())
sg = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))


for i in range(m):

    print(upper_bound(sg, card[i]) - lower_bound(sg, card[i]), end=' ')
