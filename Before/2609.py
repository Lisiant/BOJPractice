a, b = map(int, input().split())
max_num = max(a, b)
min_num = min(a, b)

tmp = 1
while tmp:
    tmp = max_num % min_num
    max_num = min_num
    min_num = tmp

gcd = max_num

lcm = abs(a*b) // gcd
print(gcd)
print(lcm)
