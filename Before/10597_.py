import sys
input = sys.stdin.readline


def solve(cur):

    if cur >= len(s):
        print(*arr)
        exit()

    if cur + 1 <= len(s):
        num = int(s[cur])
        if num <= n:
            if not vis[num]:
                vis[num] = True
                arr.append(num)
                solve(cur + 1)
                arr.pop()
                vis[num] = False

    if cur + 2 <= len(s):
        num = int(s[cur] + s[cur+1])
        if num <= n:
            if not vis[num]:
                vis[num] = True
                arr.append(num)
                solve(cur + 2)
                arr.pop()
                vis[num] = False


arr = []
vis = [False for _ in range(90)]
s = input().rstrip()

if len(s) <= 9:
    n = len(s)
else:
    n = (len(s) - 9) // 2 + 9

solve(0)
