import sys
input = sys.stdin.readline

n = list(map(int, str(bin(int(input())))[2:]))
res = 0
for ch in n:
    if ch == 1:
        res += 1

print(res)
