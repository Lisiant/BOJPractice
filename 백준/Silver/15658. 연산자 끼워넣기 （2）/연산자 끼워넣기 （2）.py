import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

INF = int(1e9)

max_val, min_val = -INF, INF
n = int(input())
data = list(map(int, input().split()))
op_counts = list(map(int, input().split()))

def calc(prev, new, op):
    if op == 0:
        return prev + new
    
    if op == 1:
        return prev - new
    
    if op == 2:
        return prev * new
    
    if op == 3:
        if prev < 0:
            return -int(-prev / new)
        return prev // new            
        
    
def solve(cur, idx):
    global max_val, min_val
    
    if idx == n:
        max_val, min_val = max(max_val, cur), min(min_val, cur)
        return
    
    for i in range(4):
        
        if op_counts[i] > 0:
            op_counts[i] -= 1 
            val = calc(cur, data[idx], i)
            solve(val, idx + 1) 
            op_counts[i] += 1
        

solve(data[0], 1)
print(max_val)
print(min_val)