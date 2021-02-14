# 연속합 - 실버2

n = int(input())
arr = list(map(int,input().split()))
dp = [0 for _ in range(100001)]
dp[0] = arr[0]
result = dp[0]
for i in range(1,n):
	dp[i] = max(dp[i-1] + arr[i], arr[i])
	result = max(result, dp[i])

print(result)