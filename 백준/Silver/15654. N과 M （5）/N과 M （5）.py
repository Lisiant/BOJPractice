import sys


def solve(data, k):


    if k == m:
        for i in range(m):
            print(arr[i], end= ' ')
        print()    
        return
    
    for i in range(n):
        if not isused[i]:
            arr[k] = data[i]
            isused[i] = True
            solve(data, k+1)
            isused[i] = False
            
        

n, m = map(int, sys.stdin.readline().split())
data = sorted(list(map(int, sys.stdin.readline().split())))
isused = [False for _ in range(n)]
arr = [-1 for _ in range(m)]
solve(data, 0)
