from collections import deque

m, n = map(int, input().split())
tomatoes = []
for _ in range(n):
	tomatoes.append(list(map(int,input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
days = 0
flag = True
def bfs():
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = dx[i] + x
			ny = dy[i] + y
			if nx >= 0 and nx < n and ny >= 0 and ny < m:
				if tomatoes[nx][ny] == 0:
					tomatoes[nx][ny] = tomatoes[x][y] + 1
					queue.append((nx, ny))

queue = deque()
for i in range(n):
	for j in range(m):
		if tomatoes[i][j] == 1:
			queue.append((i,j))
bfs()
for i in range(n):
	for j in range(m):
		if tomatoes[i][j] == 0:
			flag = False
		if days < tomatoes[i][j]:
			days = tomatoes[i][j]
print(tomatoes)
print(days-1 if flag else -1)
		
