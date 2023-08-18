import sys
input = sys.stdin.readline

a, k = map(int, input().split())


if k == 0:
    print(a)
elif a % 2 ==0 :
    print(1)
else:
    print(a)
    
    