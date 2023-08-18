import sys
input = sys.stdin.readline

h,y = map(int, input().split())
d = [0] * 11
d[0] = h


for i in range(1, 11):
    
    d[i] = int(d[i-1] * 1.05)

    if i >= 3:
        d[i] = max(d[i], int(d[i-3] * 1.2))
    
    if i >= 5:
        d[i] = max(d[i], int(d[i-5] * 1.35))

print(d[y])
    



