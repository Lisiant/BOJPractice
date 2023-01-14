import sys
stk = []
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
dic = {}

for i in range(n):
    dic[data[i]] = i+1

for i in range(n):

    while len(stk) != 0:
        if stk[-1] > data[i]:
            print(dic[stk[-1]], end=' ')
            break
        stk.pop()

    if len(stk) == 0:
        print(0, end=' ')

    stk.append(data[i])

'''
스택에 들어있는 수: 나보다 큰 빌딩
'''
