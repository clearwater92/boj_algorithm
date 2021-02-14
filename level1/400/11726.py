# 2xn 타일링 - 실버3

n = int(input())
dp = [0 for _ in range(1001)]

dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n] % 10007)
