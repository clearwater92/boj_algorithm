n, m = map(int,input().split())
adj = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(m):
	x, y = map(int, input().split())
	adj[x][y] = 1
	adj[y][x] = 1

def dfs(cur):
	visited[cur] = True
	for i in range(1, n+1):
		if not visited[i] and adj[cur][i] == 1:
			dfs(i)
		if i == n:
			return;

for i in range(1, n+1):
	if not visited[i]:
		dfs(i)
		count+=1

print(count)