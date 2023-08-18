import sys
input = sys.stdin.readline

dp = [0]*105

dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, 101):
    tmp = i
    for j in range(1, i-2):
        tmp = max(tmp , dp[j]*(i-j-1))
    dp[i] = tmp        



n = int(input())
print(dp[n])