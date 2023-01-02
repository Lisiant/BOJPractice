import sys
from collections import deque
input = sys.stdin.readline


n, k = map(int, input().split())
q = deque()
res = []
idx = 1
for i in range(1, n+1):
    q.append(i)


while q:

    if idx % k == 0:
        res.append(q.popleft())
    else:
        q.append(q.popleft())
    idx += 1

temp = '<'
for i in range(n-1):
    temp += str(res[i])
    temp += ', '

temp += str(res[n-1])
temp += '>'
print(temp)
