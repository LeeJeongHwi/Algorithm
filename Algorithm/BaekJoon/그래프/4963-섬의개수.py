#8방향 탐색
from sys import stdin
import sys
sys.setrecursionlimit(10**7)

def dfs(graph,x,y,cnt):
	global w,h
	graph[x][y] = 0

	dx = [1,-1,0,0,1,1,-1,-1]
	dy = [0,0,1,-1,1,-1,1,-1]

	for i in range(8):
		n_x = x+dx[i]
		n_y = y+dy[i]

		if n_x >= 0 and n_x < h and n_y >= 0 and n_y < w:
			if graph[n_x][n_y] == 1:
				cnt = dfs(graph,n_x,n_y,cnt+1)

	return cnt


while True:
	w,h = map(int,stdin.readline().split())
	if w == 0 and h == 0:
		break

	graph = []
	for _ in range(h):
		line = list(map(int,stdin.readline().split()))
		graph.append(line)
	
	ans = []
	for i in range(h):
		for j in range(w):
			if graph[i][j] == 1:
				ans.append(dfs(graph,i,j,1))
	print(len(ans))