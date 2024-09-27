import sys, heapq

input = sys.stdin.readline

n = int(input())
cur = int(input())
data = []
res = 0
for _ in range(n - 1):
    heapq.heappush(data, int(input()) * (-1))
if len(data) == 0 :
    print(0)
    exit()

while cur <= data[0] * (-1):
    temp = heapq.heappop(data)
    temp *= (-1)
    temp -= 1
    cur += 1
    heapq.heappush(data, temp * (-1))
    res += 1

print(res)
