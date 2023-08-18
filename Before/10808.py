n = input()
data = [0 for i in range(26)]

for ch in n:
    data[ord(ch) - 97] += 1

for i in data:
    print(i, end=' ')
