import sys

input = lambda: sys.stdin.readline()

dict = {}
n = int(input())
data = []
for i in range(n):
    data.append(list(input().rstrip()))

for word in data:
    length = len(word) - 1
    for idx, ch in enumerate(word):
        if ch not in dict:
            dict[ch] = 10 ** (length - idx)
        else:
            dict[ch] += 10 ** (length - idx)

values = list(dict.values())
values.sort(reverse=True)
res = 0

temp = 9
for i in range(len(values)):
    res += values[i] * (temp - i)

print(res)
