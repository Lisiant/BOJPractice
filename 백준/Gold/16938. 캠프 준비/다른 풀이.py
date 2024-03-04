import sys

input = sys.stdin.readline

n, l, r, x = map(int, input().split())
data = list(map(int, input().split()))
combs = []
res = 0
temp = [0] * n
is_used = [False] * n


def is_valid(combination):
    if l <= sum(combination) <= r and max(combination) - min(combination) >= x:
        return True
    return False

# 기존 코드에서 combinations 라이브러리 사용하지 않은 경우
# 조합 구하기
def generate_comb(idx, cnt, limit):
    if idx == cnt:
        combs.append(temp[:cnt])
        return

    for i in range(limit, n):
        if not is_used[i]:
            is_used[i] = True
            temp[idx] = data[i]
            generate_comb(idx + 1, cnt, i + 1)
            is_used[i] = False

# n개의 항목 중에서 i개를 뽑아 조합 생성. 모든 경우의 수를 따져야 하므로 i를 반복.
for i in range(1, n+1):
    generate_comb(0, i, 0)

for comb in combs:
    if is_valid(comb):
        res += 1

print(res)
