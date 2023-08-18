import sys
input = sys.stdin.readline

n=1000000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(i+i, n+1, i):
        a[j] = False
        
        
while True:
    L, U = map(int, input().split())    
    x = y = 0
    if L == -1 and U == -1:
        break
    
    for prime in primes:
        if L <= prime <= U:
            x += 1
            if prime % 4 == 1 or prime == 2:
                y += 1
    print(L, U, x, y)
            
        