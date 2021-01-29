n = int(input())

digitCount = 0
for i in range(1, n+1):
	digitCount += len(str(i))

print(digitCount)