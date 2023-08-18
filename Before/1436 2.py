'''
n = int(input())
count = 0
num = 0
while count != n:
    num += 1
    if str(num).count('666') > 0:
        count += 1

print(num)
'''
# 다른 풀이
s = int(input())
nlist = []
n = 0
while len(nlist) <= 10000:  # n <=10000
    if not n % 10 == 6:  # 일반적인 경우 (n=1,2,15,18, ...)
        nlist.append(n*1000+666)  # n666 을 배열에 추가

    elif (n//10) % 100 == 66:  # 660XXX, 1660XXX, 2660XXX 으로 시작하는 경우
        for k in range(1000):
            nlist.append(n*1000+k)

    elif (n//10) % 10 == 6:   # 66XXX, 166XXX, 266XXX로 시작하는 경우
        for j in range(100):
            nlist.append(n*1000+600+j)

    elif n % 10 == 6:
        for i in range(10):
            nlist.append(n*1000+660+i)

    n += 1

print(nlist[s-1])
