n = int(input())
arr = [3, 5]
d = [5001] * (n+1)

d[0] = 0

for i in range(2):  # arr[i] = 각각의 화폐 단위
    for j in range(arr[i], n+1):  # j = 각각의 금액
        if d[j-arr[i]] != 5001:
            d[j] = min(d[j], d[j-arr[i]]+1)

if d[n] == 5001:
    print(-1)
else:
    print(d[n])

# 다른 풀이
N = int(input())
count = 0
while True:
    if (N % 5 == 0):
        count = count + (N // 5)
        print(count)
        break

    N = N - 3
    count = count + 1

    if (N < 0):
        print(-1)
        break
