'''
dic = {
    0: 0,
    1: 1
}


def fib(n):

    if n in dic:
        return dic[n]
    else:
        dic[n] = fib(n-1) + fib(n-2)
        return dic[n]


n = int(input())
print(fib(n))
'''
'''
# top-down: recursive - 스택오버플로우 가능

def fib(cache, n):
    if cache[n] != -1:
        return cache[n]
    if n == 0:
        cache[n] = 0
        return 0
    elif n == 1:
        cache[n] = 1
        return 1

    else:
        cache[n] = fib(cache, n-1) + fib(cache, n-2)
    return cache[n]


n = int(input())
cache = [-1 for _ in range(n+1)]
print(fib(cache, n))
'''

# bottom-up

n = int(input())
arr = [0, 1]
for i in range(2, n+1):
    value = arr[i-1] + arr[i-2]
    arr.append(value)

print(arr[n])
