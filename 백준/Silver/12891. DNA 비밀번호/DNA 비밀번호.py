# BOJ 12891
import sys

input = lambda: sys.stdin.readline()

s, p = map(int, input().split())
data = list(input().rstrip())
counts = list(map(int, input().split()))
alp_cnts = [0, 0, 0, 0]
st, en = 0, p
res = 0


def check_first_str():
    for i in range(p):
        if data[i] == 'A':
            alp_cnts[0] += 1
        elif data[i] == 'C':
            alp_cnts[1] += 1
        elif data[i] == 'G':
            alp_cnts[2] += 1
        elif data[i] == 'T':
            alp_cnts[3] += 1


def is_substring_valid():
    for i in range(4):
        if alp_cnts[i] < counts[i]:
            return False

    return True


def remove(idx):
    if data[idx] == 'A':
        alp_cnts[0] -= 1
    elif data[idx] == 'C':
        alp_cnts[1] -= 1
    elif data[idx] == 'G':
        alp_cnts[2] -= 1
    elif data[idx] == 'T':
        alp_cnts[3] -= 1


def add(idx):
    if data[idx] == 'A':
        alp_cnts[0] += 1
    elif data[idx] == 'C':
        alp_cnts[1] += 1
    elif data[idx] == 'G':
        alp_cnts[2] += 1
    elif data[idx] == 'T':
        alp_cnts[3] += 1


check_first_str()
if is_substring_valid():
    res += 1

for i in range(s - p):
    remove(i)
    add(p + i)

    if is_substring_valid():
        res += 1

print(res)
