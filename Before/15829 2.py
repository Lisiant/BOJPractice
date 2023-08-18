n = int(input())
string = input()
result = 0
tmp = 0

for i in range(n):
    tmp = ord(string[i]) - 96
    result += (tmp * (31**i))
print(result % 1234567891)
