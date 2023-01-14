a, b = input().split()
a = list(map(int, a))
b = list(map(int, b))
res = []
ans = str()

if len(a) > len(b):
    tmp_a = a
    tmp_b = b
else:
    tmp_a = b
    tmp_b = a

tmp_b = ([0] * (len(tmp_a) - len(tmp_b))) + tmp_b
carry = 0

for i in range(len(tmp_a)-1, 0, -1):
    num = tmp_a[i] + tmp_b[i] + carry
    if num >= 10:
        res.insert(0, (num % 10))
        carry = 1
    else:
        res.insert(0, num)
        carry = 0

num = tmp_a[0] + tmp_b[0] + carry
res.insert(0, num)

for ch in res:
    ans += str(ch)
print(ans)
