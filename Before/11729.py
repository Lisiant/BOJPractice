cnt = 0
data = list()


def hanoi(n, start, end):   # n개의 원판을 start 기둥에서 end 기둥으로 옮김
    global cnt
    global data

    if n > 0:
        # 각 기둥을 1, 2, 3 번째 기둥이라 했을 때 6 - start - end  == 중간 기둥
        hanoi(n-1, start, 6 - start - end)
        # 재귀적으로 구현하는 이유: 1~ n-1 번째 기둥이 중간 기둥으로 옮겨져야 n번째 기둥이 3번째 기둥으로 옮겨질 수 있기 때문

        data.append((start, end))  # 각 원판이 어느 기둥으로 옮겨졌는지 기록
        cnt += 1

    if n > 0:
        hanoi(n-1, 6-start-end, end)  # 중간 기둥으로 옮겼던 n-1 번째까지의 원판을 3번째 기둥으로 옮김


n = int(input())
hanoi(n, 1, 3)
print(cnt)
for a, b in data:
    print(a, b)
