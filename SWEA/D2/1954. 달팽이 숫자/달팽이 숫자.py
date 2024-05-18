t = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def solve(num, x, y, direction):
    if num == n * n + 1:
        return

    nx, ny = x + dx[direction], y + dy[direction]

    if not in_range(nx, ny) or grid[nx][ny] != 0:
        direction = (direction + 1) % 4
        nx, ny = x + dx[direction], y + dy[direction]

    grid[x][y] = num
    solve(num + 1, nx, ny, direction)


for tc in range(1, t + 1):
    n = int(input())
    grid = [[0] * n for _ in range(n)]
    solve(1, 0, 0, 0)

    print(f"#{tc}")
    for i in range(n):
        print(*grid[i])
