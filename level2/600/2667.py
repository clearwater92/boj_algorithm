from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

def bfs(x, y):
	queue = []
	queue.append((x,y))
	graph[x][y] = 0
	house = 1
	while len(queue):
		x, y = queue.pop()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx >= 0 and nx < n and ny >= 0 and ny < n:
				if graph[nx][ny] == 1:
					graph[nx][ny] = 0
					house += 1
					queue.append((nx, ny))
	return house

apartment = 0
result = []
for i in range(n):
	for j in range(n):
		if graph[i][j] == 1:
			result.append(bfs(i,j))
			apartment += 1

print(apartment)

for a in sorted(result):
	print(a)