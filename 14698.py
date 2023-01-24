# 14698: 전생했더니 슬라임 연구자였던 건에 대하여 (Hard)

import sys
import heapq
input = sys.stdin.readline
MOD = int(1e9)+7

t = int(input())
for _ in range(t):
    n = int(input())
    energy = list(map(int,input().split()))
    res = 1
    
    if n == 1:
        print(1)
        continue
    
    heapq.heapify(energy)
    
    while len(energy) > 1:
        n1 = heapq.heappop(energy)
        n2 = heapq.heappop(energy)
    
        n3 = n1 * n2
        res = (res * (n3 % MOD)) % MOD
        heapq.heappush(energy, n3)
    
    print(res)