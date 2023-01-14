import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
temp = sorted(list(set(data)))  # 중복되는 거 제거하고 정렬

temp = {temp[i]: i for i in range(len(temp))}  # "값: 인덱스" 의 형태로 딕셔너리에 저장

print(*[temp[i] for i in data])
# *[리스트] == 리스트 언패킹
# data에 들어있는 값을 딕셔너리에 넣으면 그 값에 매칭되는 인덱스가 출력됨.

# 출력 단 다른 코드:

for element in data:
    print(temp[element], end=' ')
