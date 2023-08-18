import sys
input = sys.stdin.readline


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in dic:
        return dic[n]
    else:
        dic[n] = fib(n-1) + fib(n-2)
        return dic[n]


n = int(input())
dic = dict()
print(fib(n))
