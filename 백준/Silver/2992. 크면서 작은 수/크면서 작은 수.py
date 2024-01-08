import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


x = input().rstrip()
comp = int(x)
data = list(map(int, x))

n = len(data)
is_used = [False] * n
temp = [0] * n
res = []


def solve(idx):
    
    if idx == n:
        cur = int(''.join(list(map(str, temp))))
        if cur > comp:
            res.append(cur)
        return
    
    for i in range(n):
        if not is_used[i]:
            is_used[i] = True
            temp[idx] = data[i]
            solve(idx + 1)
            is_used[i] = False
    

solve(0)
if res:
    print(min(res))
else:
    print(0)
    
        
    