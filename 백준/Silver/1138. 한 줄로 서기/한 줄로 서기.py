import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
is_used = [False] * n
temp = [0] * n

def is_valid(temp: list):
    for i in range(1, n+1):
        cnt = 0
        cur = temp.index(i)
        
        for j in temp[:cur]:
            if j > i:
                cnt += 1
        
        if data[i-1] != cnt:
            return False
        
    return True



def solve(idx):
    if idx == n:
        if is_valid(temp):
            print(*temp)
        return

    for i in range(n):
        if not is_used[i]:
            is_used[i] = True
            temp[idx] = i + 1
            solve(idx + 1)
            is_used[i] = False


solve(0)
