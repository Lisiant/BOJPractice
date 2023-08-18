import sys
import math
input = sys.stdin.readline


def divs(x):
    arr = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:

            arr.append(i)
            arr.append(x // i)

    return sorted(list(set(arr)))


n = int(input())
nums = [int(input()) for _ in range(n)]
res = []

div_num = divs(max(nums) - min(nums))

for div in div_num[1:]:
    flag = True
    prev = nums[0] % div

    for num in nums:
        if num % div != prev:
            flag = False
            break

    if flag:
        res.append(div)


for x in res:
    print(x, end=' ')
