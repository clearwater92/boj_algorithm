from collections import deque

dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,-2,-1,1,2]


def bfs(x,y,x1,y1):
	queue = deque()
	queue.append((x,y))
	graph[x][y] = 1
	
	while queue:
		x, y = queue.popleft()
		if x == x1 and y == y1:
			return graph[x][y]-1
		for i in range(8):
			nx = dx[i] + x
			ny = dy[i] + y
			if nx >= 0 and nx < l and ny >= 0 and ny <l:
				if graph[nx][ny] == 0:
					graph[nx][ny] = graph[x][y] + 1
					queue.append((nx, ny))
tc = int(input())
result = []

for _ in range(tc):
	l = int(input())
	graph = [[0 for _ in range(l)] for _ in range(l)]
	curX, curY = map(int,input().split())
	desX, desY = map(int,input().split())
	count = bfs(curX, curY, desX, desY)
	result.append(count)

for a in result:
	print(a)