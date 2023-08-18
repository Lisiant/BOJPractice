'''
# 1018

n, m = map(int, input().split())
board = []
minimum = []
for _ in range(n):
    board.append(input())


for a in range(n-8+1):
    for b in range(m-8+1):
        idx1 = 0  # B로 시작했을 때
        idx2 = 0  # W로 시작했을 때
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'B':
                        idx1 += 1
                    if board[i][j] != 'W':
                        idx2 += 1
                else:
                    if board[i][j] != 'W':
                        idx1 += 1
                    if board[i][j] != 'B':
                        idx2 += 1

        minimum.append(idx1)
        minimum.append(idx2)

print(min(minimum))

# 1181

n = int(input())
data = []
temp = []
for _ in range(n):
    data.append(input())
data = list(set(data))

for item in data:
    temp.append((len(item), item))

temp.sort()
# sort()는 len(j), j 에서 앞을 먼저 정렬후에 앞의 조건이 일치하면 뒤를 정렬한다.

for length, word in temp:
    print(word)
'''
