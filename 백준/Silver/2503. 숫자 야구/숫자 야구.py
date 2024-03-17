import sys
from itertools import permutations

input = lambda: sys.stdin.readline()

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
res = 0


def is_num_valid(num):
    for query, strike, ball in data:
        query_list = list(map(int, str(query)))

        strike_cnt, ball_cnt = 0, 0

        for i in range(3):
            if query_list[i] in num:
                if query_list[i] == num[i]:
                    strike_cnt += 1
                else:
                    ball_cnt += 1

        if strike_cnt != strike or ball_cnt != ball:
            return False

    return True


nums = [i for i in range(1, 10)]
perms = permutations(nums, 3)
for num in perms:

    if is_num_valid(list(num)):
        res += 1

print(res)
