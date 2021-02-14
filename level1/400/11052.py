# 카드 구매하기 - 실버 1
n = int(input())
card = list(map(int, input().split()))
card.insert(0, 0)
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
	for j in range(1, i+1):
		dp[i] = max(dp[i], dp[i-j] + card[j])

print(dp[n])