import sys
from collections import deque

input = lambda: sys.stdin.readline()


n, k = map(int, input().split())
arr = deque()

for i in range(2**(n-1)):
    arr.append((i, 2**n - 1 - i))
    

while arr:
    res = []
    
    for i in range(2**(k-1)):
        a, b = arr.popleft()
        res.append(a)
        res.append(b)
    
    print(*sorted(res))
        