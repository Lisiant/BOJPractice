import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
res = 0
for _ in range(n):
    heapq.heappush(heap, int(input()))

if n == 1:
    print(0)
    exit()

while True:
    if len(heap) < 2:
        break
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    res += (a+b)
    heapq.heappush(heap, a+b)
        
print(res)