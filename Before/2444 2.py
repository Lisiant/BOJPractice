n = int(input())

for i in range(1, n):
    for j in range(n-i):
        print(" ", end='')
    for k in range(2*i-1):
        print("*", end='')
    print(end='\n')


for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end='')

    for k in range(2*i-1):
        print("*", end='')
    print(end='\n')
