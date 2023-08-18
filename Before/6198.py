import sys
input = sys.stdin.readline

stk1 = []
lst = [0] * 80005
idx = 0
res = 0

n = int(input())
for _ in range(n):
    x = int(input())
    stk1.append(x)
    
lst[idx] = stk1.pop()


while stk1:    
    if stk1[-1] > lst[idx]:
        res += 1
        idx -= 1
        if idx < 0:
            idx += 2
            lst[idx] = stk1.pop()
            continue
    
    else:
        idx += 1
        lst[idx] = stk1.pop()
        
        
        
        
print(res)