'''
import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
print(a/b)

import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
print(a-b)

data = map(int, input().split())
result = 0
for element in data:
    result += (element**2)


result = result % 10
print(result)

import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a % b)

char = input()
print(ord(char))

a, b = map(int, input().split())
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")

year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("1")
else:
    print("0")

score = int(input())
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end='')
    print()

n = int(input())
for i in range(n):
    for k in range(n-1, i, -1):
        print(" ", end='')
    for j in range(i+1):
        print("*", end='')
    print()

n = int(input())
for i in range(1, 9+1):
    print("{} * {} = {}".format(n, i, n*i))

n = int(input())
for i in range(1, n+1):
    print(i)

n = int(input())
for i in range(n, 0, -1):
    print(i)

h, m = map(int, input().split())

alarm_h = h
alarm_m = m - 45
if alarm_m < 0:
    alarm_h -= 1
    alarm_m += 60
    if alarm_h < 0:
        alarm_h += 24

print(alarm_h, alarm_m)

n = int(input())
data = list(map(int, input().split()))

min_num = data[0]
max_num = data[0]
for i in range(n):
    if min_num >= data[i]:
        min_num = data[i]
for i in range(n):
    if max_num <= data[i]:
        max_num = data[i]
print(min_num, max_num)


n, x = input().split()
a = list(map(int, input().split()))

n = int(n)
x = int(x)

for element in a:
    if x > element:
        print(element, end=' ')

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(a + b)

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    # EOFError 발생시키기: ctrl + z (in windows), ctrl + d (in linux)
    except EOFError:
        break

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    print(a+b)

import sys

string = sys.stdin.readline().rstrip().split()
print(len(string))


string = input().split()
print(len(string))

data = []

for i in range(9):
    a = int(input())
    data.append(a)

max_num = data[0]
count = 0

for i in range(9):
    if max_num <= data[i]:
        max_num = data[i]
        count = i+1

print(max_num)
print(count)

a = int(input())
b = int(input())
c = int(input())
mul = str(a * b * c)
mul = list(map(int, mul))

index = []
for i in range(10):
    index.append(0)

for num in mul:
    for i in range(10):
        if num == i:
            index[i] += 1

for number in index:
    print(number)

t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)
    p = []
    for i in range(len(s)):
        p.append(s[i] * r)

    for item in p:
        print(item, end='')
    print()


a, b = input().split()
arr_a, arr_b = [], []
val_a, val_b = "", ""

for i in range(3):
    arr_a.append(a[i])
    arr_b.append(b[i])

arr_a.reverse()
arr_b.reverse()

for i in range(3):
    val_a = val_a + arr_a[i]
    val_b = val_b + arr_b[i]

val_a = int(val_a)
val_b = int(val_b)

if val_a <= val_b:
    print(val_b)
else:
    print(val_a)

scale = list(map(int, input().split()))

ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]

if scale == ascending:
    print("ascending")
elif scale == descending:
    print("descending")
else:
    print("mixed")

data = []
val = []

for i in range(10):
    data.append(int(input()) % 42)

for num in data:
    if num not in val:
        val.append(num)

print(len(val))

# 다른 풀이
a = [False] * 42
for _ in range(10):
    a[int(input()) % 42] = True

print(sum(a))

n = int(input())

for i in range(n):
    case = []
    val = str(input())
    for j in range(len(val)):
        case.append(val[j])

    score = 0
    result = 0

    if case[0] == 'O':
        score = 1
        result = 1

    for k in range(1, len(val)):
        if case[k] == 'O':
            if case[k-1] == 'O':
                score += 1
                result += score
            else:
                result += 1
                score += 1

        else:
            score = 0

    print(result)


# 다른 풀이
n = int(input())
for i in range(n):
    A = input()
    score = 0
    cnt = 1
    for i in A:
        if i == 'O':
            score = score + cnt
            cnt = cnt+1
        else:
            cnt = 1
    print(score)


data = []
for i in range(26):
    data.append(-1)

a = input()
for i in a:
    for j in range(26):
        if i == chr(97+j):
            data[j] = a.index(i)

for item in data:
    print(item, end=' ')

n = int(input())
data = input()
res = 0

for num in data:
    num = int(num)
    res += num
print(res)

n = input().upper()

alp = []
cnt = 0
for i in range(26):
    alp.append(0)

for ch in n:
    for j in range(26):
        if ch == chr(65+j):
            alp[j] += 1

max_num = max(alp)

for num in alp:
    if num == max_num:
        cnt += 1

if cnt > 1:
    print("?")
else:
    print(chr(65 + alp.index(max_num)))

# 다른 풀이
words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])



n = int(input())
data = list(map(int, input().split()))
new_data = []
max_score = max(data)

for score in data:
    new_data.append((score/max_score) * 100)

print(sum(new_data) / len(new_data))

x, y, w, h = map(int, input().split())

n = 0
res = 0
while True:
    if x+n == w:
        res = n
        break
    elif x-n == 0:
        res = n
        break
    elif y+n == h:
        res = n
        break
    elif y-n == 0:
        res = n
        break
    else:
        n += 1

print(res)

# 다른 풀이
x, y, w, h = map(int, input().split())
print(min([x, y, w-x, h-y]))

t = int(input())

for i in range(t):
    h, w, guest = map(int, input().split())
    if guest % h != 0:
        guest_floor = guest % h
        guest_room = guest // h + 1
    else:
        guest_floor = h
        guest_room = guest // h

    if guest_room < 10:
        room_num = str(guest_floor) + '0' + str(guest_room)
    else:
        room_num = str(guest_floor) + str(guest_room)

    print(room_num)

n, m = map(int, input().split())
val = []
result = []
card = list(map(int, input().split()))

for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            val.append(card[i]+card[j]+card[k])

val = list(set(val))

for num in val:
    if num <= m:
        result.append(num)


print(max(result))


while True:
    n = input()

    if int(n) == 0:
        break

    arr = []
    reverse_arr = []
    for ch in n:
        arr.append(ch)

    for i in range(len(arr)):
        reverse_arr.append(arr[len(arr)-1-i])

    if arr == reverse_arr:
        print("yes")
    else:
        print("no")

import math
n, k = map(int, input().split())
print(int(math.factorial(n) / (math.factorial(n-k) * math.factorial(k))))

n, k = map(int, input().split())
per = 1

for i in range(n, n-k, -1):
    per *= i
for j in range(k, 0, -1):
    per /= j

print(int(per))
'''
