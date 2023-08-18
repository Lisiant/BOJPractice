'''
풀이
    x,y가 주어졌을 때 y-x를 distance라고 한다.
    이때 각 시행마다 가동할 수 있는 최고 속도에 비례하여 가동 횟수가 정해진다.
    최고 속도 = i 라고 하였을 때 
    1+2+3+4+...+ i +...+1 = i*(i+1) - i = i*2 이므로
    한 번 워프할 때 움직일 수 있는 최대 거리는 i^2 이다.
    또한, i에 대하여 각 시행 별로 총 워프한 횟수는 
    1 2 3 4 .. i ... 2 1 -> (2 * i - 1)번이다.
    이를 이용하여 답을 구할 수 있다.

    distance == i**2 이면  답은 그대로 2*i -1이다.
    그렇지 않은 경우에는
    총 거리에서 최대 거리만큼 빼고
    최대 속도로 나머지 거리를 얼마나 갈 수 있는지를 계산,
    즉 (나머지 거리/ 최대 속도)을 올림하고 워프한 횟수에 더해 주면
    우리가 구하고자 하는 '최소한의 워프 횟수' 가 나온다.
'''
import math

t = int(input())
res = 0

for _ in range(t):
    x, y = map(int, input().split())
    distance = y - x
    maxspeed = 1
    while maxspeed ** 2 <= 2**31:
        if (maxspeed ** 2) < distance < (maxspeed + 1) ** 2:
            res = 2 * maxspeed - 1
            remain = distance - (maxspeed ** 2)
            res += math.ceil(remain / maxspeed)
            break
        elif (maxspeed**2) == distance:
            res = 2 * maxspeed - 1
            break
        else:
            maxspeed += 1
    print(res)
