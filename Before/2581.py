import math

m = int(input())
n = int(input())
array = [0 for i in range(n+1)]
for i in range(2, int(math.sqrt(n))+1):
    j = 2
    while i*j <= n:
        array[i*j] = 1
        j += 1

total = 0
min_num = 0
for i in range(m, len(array)):
    if i > 1:
        if array[i] == 0:
            total += i

if total == 0:
    print(-1)
else:

    print(total)
    for i in range(m, len(array)):
        if i > 1:
            if array[i] == 0:
                print(i)
                break
