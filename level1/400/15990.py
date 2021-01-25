dp = [[0, 0, 0, 0] for i in range(100001)]
dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]

for i in range(4, 100001):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % 1000000009
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % 1000000009
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % 1000000009
t = int(input())
arr = []
for _ in range(t):
	arr.append(int(input()))

for el in arr:
	print(sum(dp[el])%1000000009)