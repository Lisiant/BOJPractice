'''
import sys

n = sys.stdin.readline().rstrip()
digit = len(n)
n = int(n)
data = []

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        if 100001 * a + 10001*b + 1001*c + 101*d + 11*e + 2*f == n:
                            data.append(100000*a + 10000*b +
                                        1000*c + 100*d + 10*e + f)


data.sort()
if len(data) != 0:
    print(data[0])
else:
    print(0)
'''


import sys


def func(m, n):
    for i in range(m, n+1):
        if n == i + sum(map(int, str(i))):
            return i

    return 0


n = sys.stdin.readline().rstrip()
digit = len(n)
n = int(n)
m = max(n - 9 * digit, 0)

result = func(m, n)

print(result)
