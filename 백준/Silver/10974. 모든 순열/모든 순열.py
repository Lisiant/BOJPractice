import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
is_used = [False] * n
temp = [0] * n

def solve(idx):
    
    if idx == n:
        print(*temp)
        return
    
    for i in range(n):
        if not is_used[i]:
            is_used[i] = True
            temp[idx] = i+1
            solve(idx + 1)
            is_used[i] = False
            
solve(0)

