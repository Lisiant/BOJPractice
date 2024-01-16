import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
is_used = [False] * 10
temp = [0] * 10
res = []

def convert(arr, idx):
    
    return int(''.join(map(str, arr[::-1]))) if arr else -1
            
    

def solve(k, idx, end):
    
    if k == end:
        res.append(convert(temp, end))
        
        return
    
    for i in range(idx, 10):
        if not is_used[i]:
            is_used[i] = True
            temp[k] = i
            solve(k+1, i+1, end)
            is_used[i] = False

for i in range(1, 11):            
    solve(0,0,i)   
    
res.sort()
result = res[n] if n < len(res) else -1
print(result)
