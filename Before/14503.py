import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 1


def dfs(x, y, d, cnt):
    global res
    stk = [(x, y, d, cnt)]
    nx, ny = 0, 0

    while stk:
        cur_x, cur_y, cur_d, cur_cnt = stk.pop()

        if cur_cnt >= 4:
            if cur_d == 0:
                nx = cur_x + dx[2]
                ny = cur_y + dy[2]
            elif cur_d == 1:
                nx = cur_x + dx[3]
                ny = cur_y + dy[3]
            elif cur_d == 2:
                nx = cur_x + dx[0]
                ny = cur_y + dy[0]
            elif cur_d == 3:
                nx = cur_x + dx[1]
                ny = cur_y + dy[1]

            if graph[nx][ny] == 1:
                return res
            else:
                stk.append((nx, ny, cur_d, 0))
                continue

        vis[cur_x][cur_y] = True
        left = (cur_d -1) % 4
        nx = cur_x + dx[left]
        ny = cur_y + dy[left]

        if nx > n or ny > m or nx < 0 or ny < 0:
            continue

        if graph[nx][ny] == 1 or vis[nx][ny]:
            stk.append((cur_x, cur_y, left, cur_cnt + 1))
            continue

        stk.append((nx, ny, left, 0))
        res += 1


n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
vis = [[False] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

dfs(r, c, d, 0)
print(res)
