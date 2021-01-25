"""
# 큐 이용(rotate함수) 192ms
from collections import deque
n, k = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
res = []
while queue:
	#queue.rotate(-k+1)
	res.append(str(queue.popleft()))
#	el = queue.popleft()


print("<"+", ".join(res)+">")
"""
"""
#리스트 이용 112ms
n, k = map(int, input().split())
arr = list(range(1, n+1))
res = []
index = 0
while arr:
	index = (index + k - 1)%len(arr)
	res.append(str(arr.pop(index)))

print('<'+', '.join(res)+'>')
"""
#큐 이용 416ms
#k마다 루프 돌리고 사람이 남았는지 확인
#k-1번 빼고 넣고, 1번 결과문자열에 붙임
from collections import deque
n,k = map(int, input().split())
people = deque([i for i in range(1,n+1)])

result= '<'
while people:
	for i in range(k-1):
		people.append(people.popleft())
	result+=str(people.popleft())
	if people:
		result += ', '
	else:
		result += '>'
print(result)
