import sys
n = int(sys.stdin.readline())
data = []
temp = []
for i in range(n):
    data.append(sys.stdin.readline().rstrip())

data = list(set(data))

for string in data:
    temp.append((len(string), string))


temp.sort(key=lambda x: (x[0], x[1]))

for x, y in temp:
    print(y)
