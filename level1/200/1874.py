#직접 +(푸시), -(팝)을 코드로 구현해나가면서 해보면 쉽다
#
n = int(input())
isNo = False
stack = []
res = []
count = 0
for i in range(n):
	x = int(input())
	while count < x:
		count+=1
		stack.append(count)
		res.append('+')
	if stack[-1] == x:
		stack.pop()
		res.append('-')
	else:
		isNo = True
		break
if isNo:
	print("NO")
else:
	print("\n".join(res))
	
