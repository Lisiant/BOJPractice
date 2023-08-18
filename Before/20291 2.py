import sys
input = sys.stdin.readline

dic = {}
arr = []

n = int(input())
for _ in range(n):
    name = list(input().rstrip().split('.'))

    if name[1] not in dic:
        dic[name[1]] = 1
        arr.append(name[1])
    else:
        dic[name[1]] += 1

arr.sort()

for key in arr:
    print(key, dic[key])
