import sys

input = lambda: sys.stdin.readline()
INF = int(1e9)

n = int(input())
tastes = []
vis = [False] * n
temp = [0] * n
diff = INF

for _ in range(n):
    tastes.append(list(map(int, input().split())))


def generate(idx, k):
    global diff

    if idx == k:
        s, b = calc(temp, k)
        diff = min(diff, abs(s - b))
        return

    for i in range(idx, n):

        if not vis[i]:
            vis[i] = True
            temp[idx] = i
            generate(idx + 1, k)
            vis[i] = False


def calc(temp, k):
    s, b = 1, 0
    for i in range(k):
        s *= tastes[temp[i]][0]
        b += tastes[temp[i]][1]
    return s, b


for i in range(1, n + 1):
    generate(0, i)
print(diff)
