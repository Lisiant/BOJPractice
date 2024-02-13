import sys

input = lambda: sys.stdin.readline()

n, d, k, c = map(int, input().split())
data = [int(input()) for _ in range(n)]
results = []
dic = dict()

for i in range(k):
    if data[i] in dic:
        dic[data[i]] += 1
    else:
        dic[data[i]] = 1

res = len(dic.keys())
if c not in dic:
    res += 1

for i in range(n):
    st, en = i, (k + i) % n

    dic[data[st]] -= 1
    if dic[data[st]] == 0:
        dic.pop(data[st])

    if data[en] in dic:
        dic[data[en]] += 1
    else:
        dic[data[en]] = 1

    temp = len(dic.keys())
    if c not in dic:
        temp += 1

    res = max(res, temp)

print(res)
