'''
import sys

n = int(input())

is_valid = 0

for _ in range(n):
    data = sys.stdin.readline().rstrip()

    size = 0

    for i in range(len(data)):
        if data[i] == '(':
            size += 1
        else:
            size -= 1

            if size < 0:
                is_valid = 0
                break

    if size == 0:
        print("YES")
    elif is_valid:
        print("NO")
    else:
        print("NO")


# 다른 풀이
'''


def check(string):
    length = len(string)
    stack = list()

    for i in range(length):
        ch = string[i]
        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False

    if len(stack) != 0:
        return False
    else:
        return True


n = int(input())
for i in range(n):
    data = input()

    if check(data):
        print("YES")
    else:
        print("NO")
