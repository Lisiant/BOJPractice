import sys
input = sys.stdin.readline
INF = int(1e9)


n, m = map(int, input().split())
s = list(map(int, input().split()))
is_s = [False] * (1005)
res = INF

for num in s:
    is_s[num] = True

for i in range(1, 1001):
    if is_s[i]:
        continue
    for j in range(1, 1001):
        if is_s[j]:
            continue
        for k in range(1, 1002):
            if is_s[k]:
                continue
            res = min(res, abs(n-i*j*k))

            # n+1 < i*j*k:
            if res == 0:

                break

print(res)
