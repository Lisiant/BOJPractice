import sys
sys.setrecursionlimit(10**6)
dic = {
    1: 1,
    2: 1
}


def fibonacci(n):
    if n in dic:
        return dic[n]
    else:
        output = fibonacci(n-1) + fibonacci(n-2)
        dic[n] = output
        return output


n = int(input())
print(fibonacci(n))
