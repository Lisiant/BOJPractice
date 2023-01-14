import sys


def break_even_point(a, b, c):
    n = 0
    if b >= c:
        return -1
    else:
        n = int(a/(c-b)) + 1
        return n


a, b, c = map(int, sys.stdin.readline().split())
n = break_even_point(a, b, c)
print(n)
