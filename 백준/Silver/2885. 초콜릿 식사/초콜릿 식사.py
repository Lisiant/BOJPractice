import sys

input = sys.stdin.readline

k = int(input())
data = list(bin(k))[2:]
length = len(data)
cnt_one = 0
idx = 0


for i in range(length):
    if data[i] == '1':
        cnt_one += 1

for i in range(length - 1, -1, -1):
    if data[i] == '1':
        break

    idx += 1

if cnt_one == 1:
    print(pow(2, length - 1), 0)
    exit()

print(pow(2, length), length - idx)
