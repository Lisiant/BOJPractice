from bisect import bisect_left, bisect_right
import sys

n = int(sys.stdin.readline().rstrip())
card = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

m = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

dic = dict()
cnt = 0


def count_by_range(arr, left_val, right_val):
    right_idx = bisect_right(arr, right_val)
    left_idx = bisect_left(arr, left_val)
    return right_idx - left_idx


for i in range(m):
    cnt = count_by_range(card, numbers[i], numbers[i])

    dic[numbers[i]] = cnt

for i in range(m):
    print(dic[numbers[i]], end=' ')
