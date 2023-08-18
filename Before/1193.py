import sys
x = int(sys.stdin.readline())
floor = 0
n = 0
for i in range(1, 5000):
    if x <= i*(i+1) // 2:
        floor = i
        n = x - i*(i-1) // 2
        break

if floor % 2 == 1:
    n = floor - n + 1


print("{}/{}".format(n, floor-n+1))
