n = int(input())
res = []
tmp = 0
for i in range(n):
    tmp = int(input())
    if tmp != 0:
        res.append(tmp)
    else:
        res.pop()

print(sum(res))
