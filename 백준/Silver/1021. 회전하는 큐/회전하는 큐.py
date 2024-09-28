from collections import deque
import sys

input = lambda: sys.stdin.readline()

n, m = map(int, input().split())
nums = list(map(int, input().split()))
dq = deque()
for i in range(1,n+1):
    dq.append(i)
res = 0


for num in nums:
    pivot = len(dq) // 2
    if dq[0] == num:
        dq.popleft()
        continue

    if pivot < dq.index(num):
        while dq[0] != num:
            dq.appendleft(dq.pop())
            res += 1

    else:
        while dq[0] != num:
            dq.append(dq.popleft())
            res += 1

    dq.popleft()


print(res)

