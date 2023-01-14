import sys
n = int(sys.stdin.readline().rstrip())
count = [0] * 10001

for i in range(n):
    x = int(sys.stdin.readline().rstrip())
    count[x] += 1


for i in range(len(count)):
    for j in range(count[i]):
        sys.stdout.write("{}\n".format(i))
