from sys import stdin
from collections import deque

def dfs(graph,start):
	visit=[]
	stack = [start]
	while stack:
		node = stack.pop()
		if node not in visit:
			visit.append(node)
			if node in graph: #이게 가장 ㅅㅂ 이해가안되네
				stack += sorted(list(set(graph[node])-set(visit)),reverse=True)
	return " ".join(str(i) for i in visit)

def bfs(graph,start):
	visit=[]
	dq = deque([start])
	while dq:		
		node = dq.popleft()
		if node not in visit:
			visit.append(node)
			if node in graph: #이게 가장 ㅅㅂ 이해가안되네
				dq += sorted(list(set(graph[node])-set(visit)))
	return " ".join(str(i) for i in visit)

n,m,v = map(int,stdin.readline().split())

graph = {}
#그래프 생성
for i in range(m):
	a,b = map(int,stdin.readline().split())
	if a not in graph:
		graph[a]=[b]
	elif b not in graph[a]:
		graph[a].append(b)

	if b not in graph:
		graph[b]=[a]
	elif a not in graph[b]:
		graph[b].append(a)

print(dfs(graph,v))
print(bfs(graph,v))

#아니 ㅅㅂ 이게 왜 런타임에러야 자꾸 ㅡㅡ 진짜 얼탱이가 없네