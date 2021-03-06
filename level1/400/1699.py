# 제곱수의 합 - 실버3

n = int(input())
dp = [0 for _ in range(100001)]

dp[1] = 1
for i in range(1, n+1):
	dp[i] = i
	for j in range(1, i):
		if j**2 > i:
			break
		dp[i] = min(dp[i], dp[i-j**2] + 1)
print(dp[n])