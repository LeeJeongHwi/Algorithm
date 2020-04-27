from sys import stdin
from collections import deque
t = int(stdin.readline())

def bfs(n_y,n_x,g_y,g_x,visit,n):
	q = deque()
	q.append((n_y,n_x))
	visit[n_y][n_x] = 1
	while q:
		y,x = q.popleft()

		for dy,dx in [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]:
			ny = y+dy
			nx = x+dx

			if 0<=ny<n and 0<=nx<n and visit[ny][nx] == 0:
				visit[ny][nx] = visit[y][x] + 1
				q.append((ny,nx))
				if ny == g_y and nx == g_x:
					print(visit[ny][nx]-1)
					return
				

for _ in range(t):
	n = int(stdin.readline())
	now_y, now_x = map(int,stdin.readline().split())
	goal_y, goal_x = map(int,stdin.readline().split())
	visit = [[0]*n for _ in range(n)]
	if now_y == goal_y and now_x == goal_x:
		print(0)
		continue
	bfs(now_y,now_x,goal_y,goal_x,visit,n)

