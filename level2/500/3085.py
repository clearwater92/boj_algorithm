n = int(input())
candy = []

for _ in range(n):
    candy.append([char for char in input()])

# 계산하는 로직
def candyLength():
    global result
    # 양 옆
    for i in range(n):
        count = 1
        for j in range(n-1):
            if candy[i][j] == candy[i][j + 1]:
                count += 1
            else:
                result = max(result, count)
                count = 1
        result = max(result, count)
    # 위 아래
    for i in range(n):
        count = 1
        for j in range(n-1):
            if candy[j + 1][i] == candy[j][i]:
                count += 1
            else:
                result = max(result, count)
                count = 1
        result = max(result, count)
    return result


# 한칸 바꾸는 로직
result = 0
for i in range(n):
	for j in range(n-1):
		candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
		result = candyLength()
		candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]

		candy[j][i], candy[j + 1][i] = candy[j + 1][i], candy[j][i]
		result = candyLength()
		candy[j][i], candy[j + 1][i] = candy[j + 1][i], candy[j][i]
print(result)
