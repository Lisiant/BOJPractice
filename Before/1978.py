prime = [i for i in range(1001)]


for i in range(2, 1001):
    if prime[i] == 0:
        continue

    j = i+i
    while j <= 1000:
        prime[j] = 0
        j += i


prime = sorted(list(set(prime)))
prime.pop(0)
prime.pop(0)


n = int(input())
data = list(map(int, input().split()))
cnt = 0

for num in data:
    if num in prime:
        cnt += 1

print(cnt)
