dp = [0 for _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
	dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

n = []
t = int(input())

for i in range(t):
	n.append(int(input()))

for i in n:
	print(dp[i])

