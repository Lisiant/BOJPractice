import sys
n, m, b = map(int, sys.stdin.readline().split())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
time, height = 2**63-1, 0
for h in range(257):  # 0~256 까지 h층으로 평탄화 하기 위해 지워야 하는 블록수와 채워야 하는 블록 수를 계산
    bot = top = 0  # bot = 채워야 하는 블록 수, top = 지워야 하는 블록 수
    for i in range(n):
        for j in range(m):
            if land[i][j] < h:  # h층보다 낮으면 채워야 함
                bot += h - land[i][j]
            else:   # h층보다 높으면 지워야 함
                top += land[i][j] - h

    # 채워야 하는 블록의 수가 (지워야 할 블록의 수 + 인벤토리에 있는 블록의 개수) 보다 크면 다음 층으로 넘어감
    # if bot > top + b:
    #    continue

    t = bot + top * 2
    if t <= time:
        time = t
        height = h

print(time, height)
