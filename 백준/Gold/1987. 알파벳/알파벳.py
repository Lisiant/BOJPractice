import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, input().split())
res = 0
graph = [list(input().rstrip()) for _ in range(r)]
is_alp_used = [False] * 26
is_alp_used[ord(graph[0][0]) - 65] = True


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


def dfs(x, y, cur):
    global res

    res = max(res, cur)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if not in_range(nx, ny):
            continue

        next_alp = ord(graph[nx][ny]) - 65
        if not is_alp_used[next_alp]:
            is_alp_used[next_alp] = True
            dfs(nx, ny, cur + 1)
            is_alp_used[next_alp] = False


dfs(0, 0, 0)
print(res + 1)
