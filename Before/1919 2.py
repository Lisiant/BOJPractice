a = list(input())
b = list(input())
cnt = 0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            a[i] = '0'
            b[j] = '0'


for i in range(len(a)):
    if a[i] != '0':
        cnt += 1

for i in range(len(b)):
    if b[i] != '0':
        cnt += 1

print(cnt)
