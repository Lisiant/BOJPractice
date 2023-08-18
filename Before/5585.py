import sys

input = sys.stdin.readline

n = int(input())
price = 1000 - n
coin = [500, 100, 50, 10, 5, 1]
idx = 0
res = 0

while(price > 0):
    if price >= coin[idx]:
        price -= coin[idx]
        res += 1
    else:
        idx += 1
    

print(res)



