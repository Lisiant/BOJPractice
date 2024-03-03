import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
min_cnt = abs(n - 100)

if m == 0:
    print(min(min_cnt, len(str(n))))
    exit()
data = list(map(int, input().split()))

broken = [False] * 11
for num in data:
    broken[num] = True


def is_broken(arr):
    for ch in arr:
        if broken[ch]:
            return True
    return False

# 브루트 포스
for i in range(1000001):
    cur = list(map(int, str(i)))

    if is_broken(cur):
        continue

    # 버튼으로 만들 수 있는 숫자에서 이동하는 횟수와 최솟값 비교
    min_cnt = min(min_cnt, abs(i - n) + len(cur))

print(min_cnt)
