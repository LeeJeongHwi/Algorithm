if y+1<n and visit[y+1][x] == -1 and maps[y][x] > maps[y+1][x]:
		print(1)
		dfs(y+1,x)
	elif 0<=y-1 and visit[y-1][x] == -1 and maps[y][x] > maps[y-1][x]:
		print(2)
		dfs(y-1,x)
	elif x+1<m and visit[y][x+1] == -1 and maps[y][x] > maps[y][x+1]:
		print(3)
		dfs(y,x+1)
	elif 0<=x-1  and visit[y][x-1] == -1 and maps[y][x] > maps[y][x-1]:
		print(4)
		dfs(y,x-1)