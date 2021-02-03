"""
Solution : https://joosjuliet.github.io/2667/
2667 단지번호붙이기 (Python)
(DFS)
"""

from sys import stdin
import sys
sys.setrecursionlimit(10**7)

n = int(stdin.readline())
cnt=1
def dfs(x,y,graph):
	global cnt
	graph[x][y] += 1 #간 것
	dx = [1,-1,0,0]
	dy = [0,0,1,-1]

	for i in range(4): #4방향 탐색
		n_x = x + dx[i] #다음 X 좌표
		n_y = y + dy[i] #다음 Y 좌표

		if n_x>=0 and n_x <n and n_y >= 0 and n_y <n : #배열 밖으로 빠져나가는지 확인
			if graph[n_x][n_y] == 1:
				cnt+=1
				dfs(n_x,n_y,graph)

	#4방향 탐색 후 길이 없다는 것을 확인 후 Return 
	return cnt

graph = []
#입력
for _ in range(n):
	line = stdin.readline().rstrip()
	lines = []
	for j in line:
		lines.append(int(j))
	graph.append(lines)

ans = []
for i in range(n):
	for j in range(n):
		if graph[i][j] == 1:
			cnt=1
			ans.append(dfs(i,j,graph))
ans.sort()
print(len(ans))
for i in ans:
	print(i)