"""
Solution : https://www.acmicpc.net/board/view/40535
"""
from sys import stdin
from collections import deque

n,k = map(int,stdin.readline().split())
visit = [False for _ in range(100001)]
matrix = [0 for _ in range(100001)]
dx = [1,-1,0]
def bfs(n):
	queue = deque()
	queue.append(n)
	matrix[n] = 1
	visit[n] = True
	while queue:
		now = queue.popleft()
		dx[2] = now
		for i in range(3):
			nx = now + dx[i]
			if nx < 100001 and nx >= 0:
				if visit[nx] is False and matrix[nx] == 0:
					queue.append(nx)
					matrix[nx] = matrix[now] + 1
bfs(n)
print(matrix[k]-1)