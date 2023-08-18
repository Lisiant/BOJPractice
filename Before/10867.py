import sys
n = int(sys.stdin.readline())
temp = list(map(int, sys.stdin.readline().split()))
pos = list()
neg = list()

temp = sorted(set(temp))
for num in temp:
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)


for i in neg:
    print(i, end=' ')

for j in pos:
    print(j, end=' ')
