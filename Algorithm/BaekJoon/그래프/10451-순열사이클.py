from sys import stdin
import sys
sys.setrecursionlimit(10**5)

def dfs(graph,visit,now):
	visit[now] = 1
	if visit[graph[now][0]] != 1:
		dfs(graph,visit,graph[now][0])

if __name__=="__main__":
	t = int(stdin.readline())

	for _ in range(t):
		n = int(stdin.readline())
		#Reset
		graph = [[] for _ in range(n+1)]
		visit = [0 for _ in range(n+1)]
		per = list(map(int,stdin.readline().split()))
		#Append to List
		for i in range(1,n+1):
			graph[i].append(per[i-1])
		count = 0
		for i in range(1,n+1):
			if visit[i] != 1:
				dfs(graph,visit,i)
				count += 1
		print(count)