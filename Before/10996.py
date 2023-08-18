n = int(input())


for i in range(n):
    
    if n % 2 == 1:
        
        for j in range(n//2+1):
            print('* ', end='')
        print()
        for k in range(n//2):
            print(' *', end='')
        print()
    else:
        
        for j in range(n//2):
            print('* ', end='')
        print()
        for k in range(n//2):
            print(' *', end='')
        print()