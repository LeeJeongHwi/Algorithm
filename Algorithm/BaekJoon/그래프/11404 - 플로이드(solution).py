#Solution : https://claude-u.tistory.com/334
#플로이드 와샬 알고리즘
from sys import stdin

#도시의 개수
n = int(stdin.readline())
#버스의 개수
m = int(stdin.readline())

graph = [[10000000]*(n+1) for _ in range(n+1)]
for _ in range(m):
	start,end,cost = map(int,stdin.readline().split())
	graph[start][end] = min(cost,graph[start][end])

#k 거쳐가는 도시 / i 시작도시 / j 도착도시

for k in range(1,n+1):
	for i in range(1,n+1):
		for j in range(1,n+1):
			if i == j :
				graph[i][j] = 0
			else:
				graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
	for j in range(1,n+1):
		if graph[i][j] == 10000000:
			print(0,end=' ')
		else:
			print(graph[i][j],end=' ')
	print()