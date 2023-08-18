data = []
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        data.append(num)


if len(data) == 0:
    print("-1")
else:
    print(sum(data))
    print(min(data))
