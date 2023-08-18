import sys
import math

arr = [0 for i in range(10000 + 1)]
sosu = list()
arr[0] = 1
arr[1] = 1
for i in range(2, int(math.sqrt(10000)) + 1):
    j = 2
    while i*j <= 10000:
        arr[i*j] = 1
        j += 1
for i in range(len(arr)):
    if arr[i] == 0:
        sosu.append(i)


tc = int(sys.stdin.readline())
for _ in range(tc):
    n = int(sys.stdin.readline())
    a = b = 0
    temp = []
    for i in range(len(sosu)):
        if sosu[i] > n:
            temp = sosu[:i]
            break
        else:
            temp = sosu

    for i in range(len(temp)):
        a = temp[i]
        b = n - a
        if b in temp:
            if a >= b:
                break

    print(b, a)
'''

# 다른 풀이
def is_Decimal(n):
    for i in range(2,int(n**0.5)+1):
        if (n%i == 0):
            return False
    if (n==1):
        return False
    return True

T = int(input())
for t in range(T):
    num = int(input())
    key = int(num/2)
    for i in range(key,1,-1):
        if (is_Decimal(i) and is_Decimal(num-i)):
            print("%d %d"%(i,num-i))
            break
'''
'''
# 다른풀이 2
raw = [False] * 2 + [True] + [True, False] * 4999
for k in range(3, 100, 2):
    if raw[k]:
        for j in range(k * k, 10000, k):
            raw[j] = False

N = int(input())
for i in range(N):
    num = int(input())
    if num == 4: print("2 2")
    elif raw[num//2]: print("%d %d"%(num//2, num//2))
    else:
        half = num//2
        if half % 2 == 0:
            half +=1
        for j in range(half, num, 2):
            if raw[j] and raw[num - j]:
                print('%d %d'%(num-j, j))
                break

'''
