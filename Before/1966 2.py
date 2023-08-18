from collections import deque
import sys

tc = int(sys.stdin.readline())
for _ in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    data = deque(map(int, sys.stdin.readline().split()))
    doc = [i for i in range(n)]
    q = deque(i for i in range(n))
    cnt = 0

    
    while q:
        tmp = data[0]
        max_imp = max(data)    
        
        if tmp < max_imp:
            q.append(q.popleft())
            data.append(data.popleft())
            tmp = data[0]

        else:
            data.popleft()
            x = q.popleft()
            
            cnt += 1
            if x == doc[m]:
                print(cnt)
                break
        
            
    
        