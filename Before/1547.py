import sys

a, b, c = 1, 2, 3

m = int(sys.stdin.readline())
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    
    if x == a:
        if y == b:
            a, b= b, a
        elif y == c:
            a, c = c, a
    elif x == b:
        if y == a:
            a, b = b, a
        elif y == c:
            b, c = c, b
    else:
        if y == a:
            a,c = c,a
        elif y == b:
            b,c = c,b            
    
   
print(a)
    