import sys

n = int(sys.stdin.readline())
buildings = []
stk = []
cnt = 0
for i in range(n):
    buildings.append(int(sys.stdin.readline()))

for i in range(n):

    while len(stk) != 0:

        if stk[-1] <= buildings[i]:
            stk.pop()
        else:
            cnt += len(stk)  # 스택에 남아있는 빌딩: 나보다 높은 빌딩 -> 스택의 크기: 나보다 높은 빌딩의 개수
            break

    stk.append(buildings[i])

print(cnt)

'''
왼쪽에 있는 건물부터 하나씩 차례대로 본다.
해당 건물을 볼 수 있는 건물의 개수를 구함
'''
