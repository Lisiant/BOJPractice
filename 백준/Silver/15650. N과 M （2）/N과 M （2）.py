import sys


def solve(k, index):
    
    if k == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        
        return
    

    for i in range(index, n+1):
        if not isused[i]:
            arr[k] = i
            isused[i] = True
            solve(k+1, i+1)
            isused[i] = False


n, m = map(int, sys.stdin.readline().split())
isused = [False for _ in range(n+1)]
arr = [-1 for _ in range(m)]
solve(0,1)

