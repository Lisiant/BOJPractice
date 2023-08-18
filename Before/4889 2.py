import sys

tc = 0
while True:
    string = sys.stdin.readline().rstrip()
    if string[0] == '-':
        break
    stack = []
    result = 0

    for i in range(len(string)):

        if string[i] == '{':
            stack.append(string[i])

        else:
            if len(stack) == 0:
                stack.append('{')
                result += 1
            else:
                stack.pop()

    if len(stack) != 0:
        result += (len(stack) // 2)

    tc += 1
    print("{}. {}".format(tc, result))
