import sys
input = sys.stdin.readline


def gcd(a, b):
    x, y = min(a, b), max(a, b)

    if x == 0:
        return y

    return gcd(b % a, a)


def lcm(a, b):
    return a * b // gcd(a, b)


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b), gcd(a, b))
