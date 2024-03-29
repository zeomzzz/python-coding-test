import sys
input = sys.stdin.readline

N = int(input().rstrip())

dp = [0] * (N + 1)
prev = [0] * (N + 1) # 이전에 몇 번에 들렀다 왔는지
dp[1] = 0
if N >= 2 :
    dp[2] = 1
    prev[2] = 1
if N >= 3 :
    dp[3] = 1
    prev[3] = 1

if N >= 4 :
    for i in range(4, N + 1) :
        dp[i] = dp[i - 1] + 1
        prev[i] = i - 1

        if i % 3 == 0 and dp[i // 3] + 1 < dp[i] :
            dp[i] = dp[i // 3] + 1
            prev[i] = i // 3

        if i % 2 == 0 and dp[i // 2] + 1 < dp[i] :
            dp[i] = dp[i // 2] + 1
            prev[i] = i // 2

print(dp[N])

# 이전 찾기
idx = N
while idx != 0 :
    print(idx, end = " ")
    idx = prev[idx]
