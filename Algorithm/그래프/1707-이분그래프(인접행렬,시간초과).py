import sys
from sys import stdin

sys.setrecursionlimit(10**7)

k = int(stdin.readline())
#True == "RED" , FALSE == "BLUE"

color= True
flag = True
def dfs(graph,start,visit):
	global v
	global color
	global flag
	visit[start] = color
	color = not(color)
	for i in range(1,v+1):
		if graph[start][i] == 1 and visit[i] is None:
			dfs(graph,i,visit)
		elif graph[start][i] == 1 and visit[i] is not None:
			if visit[start] == visit[i]:
				flag = False
				return
for i in range(k):
	flag = True
	v,e = map(int,stdin.readline().split())
	graph = [[0 for _ in range(v+1)] for _ in range(v+1)]
	for j in range(e):
		x,y = map(int,stdin.readline().split())
		graph[x][y] = 1
		graph[y][x] = 1
	visit = [None for _ in range(v+1)]
	for j in range(1,v+1):
		if visit[j] == None:
			if not(flag):
				break
			dfs(graph,j,visit)
	if flag:
		print("YES")
	else:
		print("NO")
