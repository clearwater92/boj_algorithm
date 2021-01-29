from collections import deque

result = []
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
def bfs(x, y):
	queue = deque()
	queue.append((x,y))
	graph[x][y] = 0
	while queue:
		now = queue.popleft()
		for i in range(8):
			nx = now[0] + dx[i]
			ny = now[1] + dy[i]
			if nx >=0 and nx < h and ny >=0 and ny < w:
				if graph[nx][ny] == 1:
					graph[nx][ny] = 0
					queue.append((nx, ny))

while True:
	w, h = map(int,input().split())
	if w == 0 and h == 0:
		break

	graph = [list(map(int,input().split())) for _ in range(h)]

	count = 0
	for i in range(h):
		for j in range(w):
			if graph[i][j] != 0:
				count += 1
				bfs(i,j)

	result.append(count)

for a in result:
	print(a) 