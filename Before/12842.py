import sys
input = sys.stdin.readline

n, s = map(int, input().split())
m = int(input())
time = [int(input()) for _ in range(m)]
remain = n - s
cnt = 0

for i in range(100000):
    for j in range(m):
        if i % time[j] == 0:
            cnt += 1
            if cnt >= remain:
                print(j+1)
                exit()
                
            
    
    