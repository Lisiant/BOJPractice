import sys
input = sys.stdin.readline


string = list(input().rstrip())
n = len(string)
vis = [False] * n
cnt = 0


if n % 5 != 0:
    print(-1)
    exit()


def check(start):
    global cnt
    quack = ['q', 'u', 'a', 'c', 'k']
    idx = 0
    flag = True

    for i in range(start, n):
        if string[i] == quack[idx] and not vis[i]:
            vis[i] = True
            if string[i] == 'k':
                if flag:
                    cnt += 1
                    flag = False
                idx = 0
                continue
            idx += 1


for i in range(n):
    if string[i] == 'q' and not vis[i]:
        check(i)


for i in range(n):
    if not vis[i]:
        print(-1)
        exit()

if cnt == 0:
    print(-1)
    exit()

print(cnt)
