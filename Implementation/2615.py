import sys
input = sys.stdin.readline

dir = [(-1, 0), (-1, -1), (0, -1), (1, -1),
       (1, 0), (1, 1), (0, 1), (-1, 1)]

graph = [list(map(int, input().split())) for _ in range(19)]
res = []


def is_out_of_bounds(arr):
    for x, y in arr:
        if x < 0 or y < 0 or x >= 19 or y >= 19:
            return True

    return False


def is_five(arr, cur):
    for node in arr:
        if graph[node[0]][node[1]] != cur:
            return False

    return True


def is_six(arr, dir_idx, cur):
    nsx, nsy = arr[0][0] + dir[dir_idx][0], arr[0][1] + dir[dir_idx][1]
    nex, ney = arr[4][0] + dir[dir_idx+4][0], arr[4][1] + dir[dir_idx+4][1]

    if nsx >= 0 and nsy >= 0 and nsx < 19 and nsy < 19:
        if graph[nsx][nsy] == cur:
            return True

    if nex >= 0 and ney >= 0 and nex < 19 and ney < 19:
        if graph[nex][ney] == cur:
            return True

    return False


def check(a, b):
    cur = graph[a][b]
    for i in range(4):
        line = [
            (a + 2 * dir[i][0], b + 2 * dir[i][1]),
            (a + dir[i][0], b + dir[i][1]),
            (a, b),
            (a + dir[i+4][0], b + dir[i+4][1]),
            (a + 2 * dir[i+4][0], b + 2 * dir[i+4][1]),
        ]

        dir_idx = i

        if is_out_of_bounds(line):
            continue

        if is_five(line, cur):
            if not is_six(line, dir_idx, cur):
                res.append((cur, line[0]))


for i in range(19):
    for j in range(19):
        if graph[i][j] != 0:
            check(i, j)

if len(res) == 0:
    print(0)
else:
    print(res[0][0])
    print(res[0][1][0]+1, res[0][1][1]+1)
