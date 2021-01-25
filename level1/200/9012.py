# ( 일 경우에만 스택에 넣으므로 스택 안에 들어있는 괄호가 어느 것인지는
# 고려하지 않아도 된다
# 그래서 ) 가 나오면 무조건 스택이 비어있는지만 확인하면 된다
tc = int(input())
res = []
for _ in range(tc):
	stack = []
	vps = input()
	for p in vps:
		if p == '(':
			stack.append(p)
		else:
			if len(stack) == 0:
				stack.append("NO")
				break
			else:
				stack.pop()
	if stack:
		res.append('NO')
	else:
		res.append('YES')
for a in res:
	print(a)