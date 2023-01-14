a, b = map(int, input().split())

mul = a * b
while True:
    if a % b != 0:
        a, b = b, a % b
        continue
    else:
        gcd = b
        break

lcm = mul // gcd

print(gcd)
print(lcm)
