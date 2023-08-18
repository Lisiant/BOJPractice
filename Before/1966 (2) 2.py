from collections import deque
t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    priority = deque(map(int, input().split()))
    que = deque(0 for _ in range(n))
    count = 0
    que[m] = 1

    while True:
        if priority[0] == max(priority):
            count += 1

            if que[0] != 1:
                que.popleft()
                priority.popleft()
            else:
                print(count)
                break
        else:
            priority.append(priority.popleft())
            que.append(que.popleft())

'''
t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    que = list([0 for _ in range(n)])
    count = 0  # 출력값을 저장하는 변수
    que[m] = 1  # 궁금한 문서 위치 저장

    while True:
        if priority[0] == max(priority):  # priority의 첫번째 요소가 최대중요도
            count += 1  # count 1 증가

            if que[0] != 1:  # 최대 중요도이지만 우리가 찾고자 하는 값이 아님
                que.pop(0)  # 큐에서 뺌
                priority.pop(0)  # 우선순위 리스트에서도 뺌
            else:  # 최대 중요도이고 우리가 찾고자 하는 값임
                print(count)  # 출력
                break  # 종료
        else:  # 최대 중요도가 아닐 때
            priority.append(priority.pop(0))  # 중요도 리스트에서 빼서 뒤로 보냄
            que.append(que.pop(0))  # 큐에서도 빼내고 뒤로 보냄
'''


'''
왜 못풀었을까?
    1. 큐를 꼭 deque로 구현해야 한다는 강박.
    리스트만으로도 풀 수 있는 문제였음
    근데 덱으로 해도 풀리네

    2. 로직 자체가 틀림
    너무 많은 조건을 고려하려 하다 보니 조건문이 너무 많아짐
    그렇게 되면 모든 테스트 케이스를 고려하지 못하거나
    잘못된 값이 출력됨
    
    3. 굳이 위치를 저장할 리스트를 인덱스로 생각함
    '배열에서 특정 인덱스의 값만 찾고자 하면'
    그냥 0으로 배열을 초기화하고 찾고자 하는 곳에 표시만 하자

    4. 문제를 너무 복잡하게 생각함
    문제에서 주어진 상황을 간단하게 만들어보자
    중요도가 가장 높다 -> 그게 가장 맨 앞에 오면 출력

    1. 중요도 큐의 맨 앞의 값이 중요도 최댓값이 아님
        뒤로 밀면 됨. count 변동 없음(인쇄 안함)
    2. 중요도 최댓값이 맨 앞
        count는 1 증가 (인쇄를 하니까)
        1-1. 그 상황에서 우리가 찾고 싶은 값이 아니면
            그냥 큐에서 빼면 됨
        1-2. 우리가 찾고 싶은 값이면
            count 출력하고 break

'''
