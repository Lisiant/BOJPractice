import sys

string = sys.stdin.readline().rstrip()
stk = []
result = 0

stk.append(string[0])

for i in range(1, len(string)):

    if string[i] == '(':
        stk.append(string[i])

    else:
        if string[i-1] == '(':
            stk.pop()
            result += len(stk)

        else:
            stk.pop()
            result += 1

print(result)
