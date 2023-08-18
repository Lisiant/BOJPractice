import sys
from collections import deque


n, k = map(int, sys.stdin.readline().split())
data = deque([i for i in range(1, n+1)])
res = []

while len(data) > 0:

    # 시간 초과 났었던 코드
    '''
    if cnt % k == k-1:
        cnt = 0
        res.append(data.popleft())
    else:
        cnt += 1
        data.append(data.popleft())
    '''

    for i in range(k-1):
        data.append(data.popleft())
    res.append(data.popleft())

print("<", end='')
for i in range(len(res) - 1):
    print("{}, ".format(res[i]), end='')
print("{}>".format(res[n-1]))
