from sys import stdin

count = 0
visit = []
def dfs(graph,start):
	global count
	stack = [start]
	while stack:
		node=stack.pop()
		visit.append(node)
		for i in graph[node]:
			if i not in visit+stack:
				stack.append(i)
	count+=1


n,m = map(int,stdin.readline().split())
graph = {}
for i in range(m):
	u,v = map(int,stdin.readline().split())
	if u not in graph:
		graph[u] = [v]
	elif v not in graph[u]:
		graph[u].append(v)

	if v not in graph:
		graph[v] = [u]
	elif u not in graph[v]:
		graph[v].append(u)

for i in range(1,n+1):
	if i in graph:
		if i not in visit:
			dfs(graph,i)
print(count)


# 시간초과 코드 