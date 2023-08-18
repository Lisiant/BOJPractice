data = [int(input()) for _ in range(5)]

avg = sum(data) // 5
data = sorted(data)
mid = data[2]

print(avg)
print(mid)
