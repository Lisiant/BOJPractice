import sys
input = sys.stdin.readline


n = int(input())
data = sorted(list(map(int, input().split())))

idx = n // 2
if n % 2 == 0:
    left, right = 0,0
    for i in range(n):
        left += abs(data[idx-1] - data[i])
        right += abs(data[idx] - data[i])

    if left > right:
        print(data[idx])
    else:
        print(data[idx - 1])

else:
    print(data[idx])
    # cur = 0
    # for i in range(n):
    #     cur += abs(data[idx] - data[i])

    # print()
    