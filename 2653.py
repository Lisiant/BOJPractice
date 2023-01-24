import sys
input = lambda: sys.stdin.readline()

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
tmp = [[] for _ in range(n)]
res = []
cnt = 0


for i in range(n):
    for j in range(n):
        if data[i] == data[j]:
            tmp[i].append(j)
            
            
for row in tmp:
    if len(row) == 1:
        print(0)
        exit()
        
    if row not in res:
        res.append(row)
        cnt += 1
        
                    
print(cnt)

for item in res:
    for num in item:
        print(num+1, end=' ')
    print()

