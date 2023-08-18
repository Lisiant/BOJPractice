import sys
string = sys.stdin.readline().rstrip()

data = list()

for i in range(len(string)):
    data.append(string[i:len(string)])

data = sorted(data)
for i in data:
    print(i)
