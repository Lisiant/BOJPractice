a, b, c = map(int, input().split())
won = 0

if a == b:
    if a == c:
        won = 10000 + 1000 * a
    else:
        won = 1000 + 100 * a


else:
    if b == c:
        won = 1000 + 100 * b

    elif a == c:
        won = 1000 + 100 * a

    else:
        won = max(a, b, c) * 100

print(won)
