# 카드 구매하기 2 - 실버 1

n = int(input())
card = list(map(int,input().split()))
card.insert(0, 0)
dp = [1001 for _ in range(n+1)]
for i in range(1, n+1):
	dp[i] = card[i]
	for j in range(1, i):
		dp[i] = min(dp[i], dp[i-j] + card[j])
print(dp[n])