import sys, heapq
input = sys.stdin.readline


present = []
n = int(input())
for _ in range(n):

    data = list(map(int, input().split()))
    
    
    if data[0] == 0:
        if not present:
            print(-1)
        else:
            res = -heapq.heappop(present)
            print(res)
        
    for item in data[1:]:
        heapq.heappush(present, -item)
    
    