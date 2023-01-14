n = int(input())
operand = list()
stack = list()
count = 1
temp = True

for i in range(n):
    x = int(input())

    while count <= x:
        stack.append(count)
        count += 1
        operand.append('+')

    if stack[-1] == x:
        stack.pop()
        operand.append('-')
    else:
        temp = False

if temp == False:
    print("NO")
else:
    for i in operand:
        print(i)

'''
접근:
문제에서 사용할 변수들을 초기화한다.
stack = 스택, 값을 비교하는데 쓰임
operand = +, -를 순서대로 저장하는 리스트
count = stack에 들어갈 숫자. 1씩 증가하면서 입력값과 비교
temp = 가능한지 불가능한지 정하는 bool 형태의 변수

첫번째 줄에서 받은 n값을 기준으로, n번 반복하는 for문을 돌리면서 x로 입력값을 받는다.
count가 x와 똑같을 때까지 while문을 돌리며,
count의 값을 stack에 추가하고 count에 1을 더한다. operand에는 '+'를 넣어준다.
이 때 stack에는 1부터 x까지의 숫자가 순차적으로 들어가며, 반복문이 끝날 때 count == x 이다.
stack의 마지막 값이 x와 같다면 stack에서 pop을 해주고 operand에는 '-'를 추가한다.
만약 stack의 마지막 값이 x와 같지 않다면 temp에 False를 저장한다. 
이후 for문에 의해 다음 반복으로 넘어감.

for문이 끝났을 때 temp 값이 그대로 True 라면 operand를 출력,
그렇지 않으면 NO를 출력한다.

'''
'''
생각을 못했던 부분:
    입력받는 부분을 꼭 다른 리스트에 넣어서 비교하려고 함.
    굳이 그럴 필요 없이 입력 받을 때마다 그 수를 비교하면 될 것을..
    다른 사람의 코드를 보니 리스트에 넣고 구현하긴 했다.

    힌트를 얻은 이후에도 답을 구하지 못 했던 이유는
    조건문 반복문에 대한 이해도가 떨어져서 그런 것 같다.
    반복문이 언제 끝나도록 설계하는지 등

    언제 NO를 출력해야 하는지 몰랐음:
    1. stack이 비면 operand를 출력, stack이 비지 않으면 no 출력
    2. stack의 마지막 항목이 입력값과 다르면 bool값을 False로 변경
조건문, 반복문이 전부라지만 그게 제일 어렵다..

'''
