from sys import stdin
from collections import deque
from itertools import combinations
#PyPy3 1180ms ==> 시간 효율이 매우 안좋다, python3 에서는 시간초과
n , m = map(int,stdin.readline().split())
city = [list(map(int,stdin.readline().split())) for _ in range(n)]
ch = []
house = 0
for i in range(n):
	for j in range(n):
		if city[i][j] == 2:
			ch.append((i,j))
		elif city[i][j] == 1:
			house+=1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
comb=[]
for com in combinations(ch,m): 
	comb.append(com)
def bfs(visit,queue,h):
	result = 0
	dis=1
	while queue:
		for _ in range(len(queue)):
			y,x= queue.popleft()
			for i in range(4):
				ny=y+dy[i]
				nx=x+dx[i]
				if 0<=ny<n and 0<=nx<n and visit[ny][nx]==0:
					visit[ny][nx] = 1
					if city[ny][nx] == 1:
						h+=1
						result+=dis
						# print(h,house,result)
						if h == house:
							return result
					queue.append((ny,nx))
		dis+=1
minDis = float('inf')
for c in comb:
	queue=deque(c)
	# print(queue)
	visit=[[0]*n for _ in range(n)]
	minDis = min(minDis,bfs(visit,queue,0))
print(minDis)
