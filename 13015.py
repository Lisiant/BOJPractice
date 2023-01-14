import sys

n = int(sys.stdin.readline())

print('*'*n + ' '*(2*(n-1)-1) + '*'*n)

for i in range(1, n-1):
    
    for j in range(1, i+1):
        print(' ', end='')
            
    print('*'+ ' ' * (n-2) + '*', end='')
    print(' ' * (2*(n-i)-3), end='')
    print('*'+ ' ' * (n-2) + '*', end='')           
    print()
   
   
print(' '*(n-1) + '*' + ' ' * (n-2) + '*' + ' ' * (n-2) + '*')   

for i in range(n-2, 0, -1):
    
    for j in range(i,0,-1):
        print(' ', end='')
    
    print('*'+ ' '* (n-2) + '*', end='')
    print(' ' * (2*(n-i)-3), end='')    
    print('*'+ ' '* (n-2) + '*', end='')
    print()
    
print('*'*n + ' '*(2*(n-1)-1) + '*'*n)

