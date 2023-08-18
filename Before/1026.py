'''
# 백준1026: 보물
문제에서 구해야 하는 값은 S의 '최솟값'이다.

문제에서 "B에 있는 수는 재배열하면 안 된다" 라고 하지만
A를 내 마음대로 정렬할 수 있기 때문에
A와 B 모두 정렬하고 최솟값을 구하여도 상관이 없다.

만약 문제에서 주어진 조건대로 A를 출력하라고 한다면
A를 오름차순으로 정렬하고
B의 각 원소가 몇 번째로 큰 수 인지 파악하여 순서에 맞게 넣어주면 된다. 
'''

import sys

n = int(sys.stdin.readline())

a = sorted(list(map(int, sys.stdin.readline().split())))
b = sorted(list(map(int, sys.stdin.readline().split())))


for i in range(n):
    res += a[i] * b[n-1-i]

print(res)
