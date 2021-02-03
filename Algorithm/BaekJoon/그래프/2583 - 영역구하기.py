from sys import stdin
import sys
sys.setrecursionlimit(10**9)
#재귀로 풀지 않고 while로 풀면 더 시간이 빠르게 나올 수 있음
#하지만 지금은 재귀 연습 중이므로 재귀로 풀음
n,m,k = map(int,stdin.readline().split())

maps = [[0]*(m) for _ in range(n)]

#draw Rectangle
for _ in range(k):
	x1,y1,x2,y2 = map(int,stdin.readline().split())
	y1 = abs((n-1)-y1)
	y2 = abs(n-y2)
	x1 = x1
	x2 = x2-1
	for i in range(y1,y2-1,-1):
		for j in range(x1,x2+1):
			if maps[i][j] == 1:
				 continue
			maps[i][j] = 1
	# 2,0 ~ 4,4 / 1,1 ~ 5,2 / 0,4 ~ 2,6
	# 2,0 ~ 1,3 / 3,1 ~ 0,1 / 4,4 ~ 3,5

visit= [[0]*m for _ in range(n)]
def dfs(y,x):
	global size
	visit[y][x] = 1
	for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
		ny= y+dy
		nx= x+dx
		if 0<=ny<n and 0<=nx<m and visit[ny][nx] == 0:
			if maps[ny][nx] == 0:
				dfs(ny,nx)
				size+=1
ans = []
count = 0
for i in range(n):
	for j in range(m):
		if visit[i][j] == 0 and maps[i][j] == 0:
			size=1
			count+=1
			dfs(i,j)
			ans.append(size)
# for i in visit:
# 	print(i)
ans.sort()
print(count)
print(*ans)