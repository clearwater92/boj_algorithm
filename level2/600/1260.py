from collections import deque

n, m, v = map(int, input().split())
adj = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
	x, y = map(int, input().split())
	adj[x][y] = 1
	adj[y][x] = 1

def dfs(cur):
	visited[cur] = True
	print(cur, end=' ')
	for i in range(1, n+1):
		if not visited[i] and adj[cur][i] == 1:
			dfs(i)

def bfs(start):
	queue = deque([start])
	visited[start] = True
	while queue:
		cur = queue.popleft()
		print(cur, end=' ')
		for i in range(1, n+1):
			if not visited[i] and adj[cur][i] == 1:
				queue.append(i)
				visited[i] = True

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)
print()