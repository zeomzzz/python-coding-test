import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)

for i in range(n + 1) :
    if i == 1 : dp[i] = 1
    elif i == 2 : dp[i] = 1
    elif i == 3 : dp[i] = 2
    else :
        dp[i] = dp[i-2] + dp[i-1]

print(dp[n])
