import sys
'''
#풀이 1

주어진 문자열 string을 왼쪽에서 오른쪽으로 탐색하는 index i
오른쪽에서 왼쪽으로 탐색하는 index j 가 있을 때

string[i] == string[j] 이면
i 부터 j 까지 모든 글자가 똑같아야 함
다르면 바로 return False

'''


def is_groupWord1(string):
    for i in range(len(string)):
        for j in range(len(string)-1, -1, -1):
            if string[i] == string[j]:
                for k in range(i, j):
                    if string[k] != string[k+1]:
                        return False

    return True


'''
# 풀이 2
blank라는 비어있는 str 변수를 생성
string 전체를 탐색할 때 
string[i] 가 blank에 있으면
string[i-1] == string[i] 이어야 하고 
아니면 False
그렇다면 연속된 글자이므로 blank에 추가


'''


def is_groupWord(string):
    blank = ''
    for i in range(len(string)):
        if string[i] not in blank:
            blank += string[i]

        else:
            if string[i] != string[i-1]:
                return False
            else:
                blank += string[i]
    return True


n = int(sys.stdin.readline())
count = 0

for _ in range(n):
    string = sys.stdin.readline().rstrip()
    a = is_groupWord(string)

    if a:
        count += 1


print(count)
