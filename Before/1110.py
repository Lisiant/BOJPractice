import sys

n = sys.stdin.readline().rstrip()  # 문자열로 받음

if int(n) < 10:     # n이 한자리 수 인 경우
    n = '0' + n     # 'n'을 '0n'으로 바꿔 준다.
tmp = n
cnt = 0

while True:
    b = tmp[1]  # 마지막 자리 수
    c = str((int(tmp[0])+int(b)) % 10)  # n의 각 자리수의 합의 마지막 자리 수 (문자열)
    tmp = b+c   # 문자열 사이의 + 연산을 통하여 이어 붙임
    cnt += 1
    if tmp == n:
        break

print(cnt)
