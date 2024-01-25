import sys

input = lambda: sys.stdin.readline()

alps = [0] * 26
data = list(input().rstrip())
n = len(data)
res = 0

for ch in data:
    alps[ord(ch) - 97] += 1


def solve(idx, cur):
    global res
    if idx == n:
        res += 1
        return

    for i in range(26):
        if alps[i] == 0:
            continue

        if cur != "" and i == ord(cur[-1]) - 97:
            continue

        alps[i] -= 1
        solve(idx + 1, cur + chr(i + 97))
        alps[i] += 1


solve(0, "")
print(res)
