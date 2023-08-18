import sys

string = sys.stdin.readline().rstrip()
stack = list()
res = 0
temp = 1
impossible = False


def empty():
    if len(stack) == 0:
        return True
    else:
        return False


for i in range(len(string)):
    if string[i] == '(':
        stack.append(string[i])
        temp *= 2

    elif string[i] == '[':
        stack.append(string[i])
        temp *= 3

    elif string[i] == ')':
        if empty() or stack[-1] != '(':
            impossible = True
            break
        else:
            if string[i-1] == '(':  # ()
                res += temp
            stack.pop()
            temp = temp // 2

    elif string[i] == ']':
        if empty() or stack[-1] != '[':
            impossible = True
            break
        else:
            if string[i-1] == '[':  # []
                res += temp
            stack.pop()
            temp = temp // 3


if not empty():
    impossible = True

if impossible:
    print(0)
else:
    print(res)

'''
temp = 1로 두고 2나 3을 곱하고 나누는 것으로 문제를 풀었다.
우선 주어진 문자열이 올바른지 아닌지는 이전의 여러 문제들을 통해 알 수 있었다.

<문자열을 탐색하는 도중>
1. 비어있는 스택에서 pop 하려 할 때
2. ([)] 와 같이 짝이 맞지 않는 괄호를 pop 하려 할 때

<문자열 탐색이 끝난 후>
1. 스택이 비어있지 않을 때

올바른 문자열이 주어졌을 때, 이 문제 풀이에서 사용한 알고리즘은 다음과 같다.

1. '(' 가 입력된 경우: 스택에 append, temp *= 2
2. '[' 가 입력된 경우: 스택에 append, temp *= 3
3. ')' 가 입력된 경우: 
    3-1. 바로 이전에 입력된 값이 '(' 인 경우:
        temp를 결과값에 더함
    
    스택에서 pop, temp /= 2
4. ']' 가 입력된 경우:
    4-1. 바로 이전에 입력된 값이 '[' 인 경우:
        temp를 결과값에 더함
    
    스택에서 pop, temp /= 3

분배법칙을 이용한 것과 같다.
ex) (()[[]])
위 괄호열을 계산하면
2 * (2 + 9) = 22 이다.
이는 4 + 18 과 같다.

너무 덧셈과 곱셈에만 집착하지 말고, 나누기를 이용하는 방법도 있음을 생각하자.
'''
