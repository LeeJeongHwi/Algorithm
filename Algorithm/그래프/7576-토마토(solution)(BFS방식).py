"""
Solution : https://chocodrogba.tistory.com/11
"""
from collections import deque
from sys import stdin

n,m = map(int,stdin.readline().split())

def bfs(graph):
	queue = deque()
	dx = [1,-1,0,0]
	dy = [0,0,1,-1]
	result = -1
	#처음 1인 값을 QUEUE에 append
	for i in range(m):
		for j in range(n):
			if graph[i][j] == 1:
				queue.append([i,j])
	while queue:
		result += 1
		qulen = len(queue)
		for _ in range(qulen):
			y,x=queue.popleft()
			
			for i in range(4):
				nx = x+dx[i]
				ny = y+dy[i]
				if nx>=0 and nx < n and ny >= 0 and ny < m:
					if graph[ny][nx] == 0:
						graph[ny][nx] = 1
						queue.append([ny,nx])
	for i in range(m):
		for j in range(n):
			if graph[i][j] == 0:
				return -1
	return result

graph = []
for _ in range(m):
	line = list(map(int,stdin.readline().split()))
	graph.append(line)
print(bfs(graph))