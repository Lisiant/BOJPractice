import sys


def check(string):
    length = len(string)
    stack = list()

    for i in range(length):
        ch = string[i]
        if ch == '(':
            stack.append(ch)

        elif ch == '[':
            stack.append(ch)

        elif ch == ')':
            if len(stack) != 0:
                if stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            else:
                return False

        elif ch == ']':
            if len(stack) != 0:
                if stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            else:
                return False
        else:
            pass

    if len(stack) != 0:
        return False
    else:
        return True


string = str()
while True:
    string = sys.stdin.readline().rstrip()
    if string == '.':
        break

    if check(string):
        print("yes")
    else:
        print("no")
