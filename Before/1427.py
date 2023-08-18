import sys

num = sys.stdin.readline().rstrip()
temp = list()
for i in num:
    temp.append(int(i))

temp.sort()

for i in range(len(temp)-1, -1, -1):
    print(temp[i], end='')
