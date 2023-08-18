import sys
import math

arr = [0 for i in range(2 * 123456 + 1)]
arr[0] = 1
arr[1] = 1
for i in range(2, int(math.sqrt(2 * 123456)) + 1):
    j = 2
    while i * j <= 2 * 123456:
        arr[i*j] = 1
        j += 1

while True:
    x = int(sys.stdin.readline())
    if x == 0:
        break
    cnt = 0
    for i in range(x+1, 2*x + 1):
        if arr[i] == 0:
            cnt += 1
    print(cnt)
