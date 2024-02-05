import sys
from collections import deque

input = lambda: sys.stdin.readline()

n = int(input())
q = deque()
dic = dict()
data = []

for i in range(n):
    name, num_str = map(str, input().split())
    num = int(num_str)
    dic[name] = num

    q.append(name)

while len(q) >= 2:
    cur = q.popleft()

    for i in range(dic[cur] - 1):
        q.append(q.popleft())

    q.popleft()

print(q[0])