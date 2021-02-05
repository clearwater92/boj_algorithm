from collections import deque

n, m = map(int,input().split())

haze = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for i in range(n):
	haze.append(list(map(int, input())))

def bfs(x, y):
	queue = deque()
	queue.append((x,y))
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = dx[i] + x
			ny = dy[i] + y
			if nx >= 0 and nx < n and ny >= 0 and ny < m:
				if haze[nx][ny] == 1:
					haze[nx][ny] = haze[x][y] + 1
					queue.append((nx, ny))
	return haze[n-1][m-1]

print(bfs(0,0))