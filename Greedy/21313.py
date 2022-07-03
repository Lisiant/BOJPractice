import sys
input = sys.stdin.readline

n = int(input())
num = n // 2

if n % 2 == 0:
    res = ("1 2 " * num)
else:
    res = ("1 2 " * num)
    res += '3'

print(res)
