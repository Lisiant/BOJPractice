import sys
input = sys.stdin.readline

vowels = ['a', 'e', 'i', 'o', 'u']
l, c = map(int, input().split())
data = sorted(list(input().split()))
is_used = [False] * c
temp = [''] * l

def has_vowel(arr):
    for i in range(l):
        for vowel in vowels:
            if arr[i] == vowel:
                return True
            
    return False
    
def has_cons(arr):
    vowel_cnt = 0

    for vowel in vowels:
        vowel_cnt += arr.count(vowel)
    
    return l - vowel_cnt >= 2


def solve(k, idx):
    
    if k == l:
        if has_vowel(temp) and has_cons(temp):
            print(''.join(temp))
        return
    
    for i in range(idx, c):
        if not is_used[i]:
            is_used[i] = True
            temp[k] = data[i]
            solve(k + 1, i + 1)
            is_used[i] = False
            
            
solve(0, 0)


