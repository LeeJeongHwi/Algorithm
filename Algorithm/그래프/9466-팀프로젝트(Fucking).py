from sys import stdin
import sys
sys.setrecursionlimit(10**7)

# 첫번째 조건 s1 -> s1
# 두번째 조건 s1 -> s2 -> s3 .... Sr-1 -> Sr -> s1



def dfs(graph,visit,done,now):
	visit[now] = 1
	if graph[now][0] == 0:
		dfs(graph,visit,done,graph[now][0],start)
	elif done[now] == 0:
		i = graph[now][0]
		


	done[now] = 1
		

t = int(stdin.readline())
for _ in range(t):
	n = int(stdin.readline())
	graph = [[] for _ in range(n+1)]
	visit = [0 for _ in range(n+1)]
	done = [0 for _ in range(n+1)]

	arr = list(map(int,stdin.readline().split()))
	for i in range(len(arr)):
		graph[i+1].append(arr[i])
	print(graph)
	count = 0
	for i in range(1,n+1):
		if visit[i] == 0:
			ct = 0
			dfs(graph,visit,done,i)