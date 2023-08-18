n = int(input())

for i in range(1, n):
    
    for j in range(n-i, 0, -1):
        print(' ', end='')
    
    print('*', end='')

    
    for k in range(2*(i-1) -1):    
        print(' ', end='')
    
    if i > 1:
        print('*', end='')    
        
    print()
    
print("*"*(2*n-1), end='')