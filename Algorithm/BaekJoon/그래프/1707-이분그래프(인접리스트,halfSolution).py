import sys
from sys import stdin

sys.setrecursionlimit(10**7)

ans = True
def dfs(graph,visit,now,check):
	global ans
	check *= -1
	visit[now] = check
	for i in graph[now]:
		if visit[i] is None :
			dfs(graph,visit,i,check)
		elif visit[i] is not None and visit[i] == visit[now]:
			ans = False
			return

if __name__ == '__main__':
	k = int(stdin.readline())
	for _ in range(k):
		v,e = map(int,stdin.readline().split())
		graph = [[] for _ in range(v+1)]
		ans = True
		for i in range(e):
			x,y = map(int,stdin.readline().split())
			graph[x].append(y)
			graph[y].append(x)
		check = -1
		visit = [None for _ in range(v+1)]
		for i in range(1,v+1):
			if visit[i] is None:
				if ans is False:
					break
				dfs(graph,visit,i,check)
		print("YES" if ans else "NO")