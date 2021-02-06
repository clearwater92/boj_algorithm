n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(1, 1001)]
result = 1
for i in range(n):
	outer = arr[i]
	for j in range(i):
		inner = arr[j]
		if outer > inner:
			dp[i] = max(dp[i], dp[j] + 1)
	result=max(result, dp[i])
print(result)