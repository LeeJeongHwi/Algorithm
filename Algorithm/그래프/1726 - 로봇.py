#참고 : https://hibee.tistory.com/161
from sys import stdin
from collections import deque
def change_Dirs(d,i):
	if i == 1: #시계 방향
		if d == 1:
			return 3
		elif d == 2:
			return 4
		elif d == 3:
			return 2 
		else:
			return 1
	elif i == 2: #반시계 방향
		if d == 1:
			return 4
		elif d == 2:
			return 3
		elif d == 3:
			return 1 
		else:
			return 2

dy =[0,0,0,1,-1]
dx =[0,1,-1,0,0]
def bfs(visit):
	queue = deque()
	queue.append((start_Y,start_X,start_dir,0))
	visit[start_Y][start_X][start_dir] = 0
	while queue:
		y,x,d,ins = queue.popleft()
		# print("now y ,now x, now d , now int",y,x,d,ins)
		if y == end_Y and x == end_X and d == end_dir:
			print(ins)
			# for i in visit:
			# 	print(i)
			return
		for i in range(1,4):
			#방향에 해당하는 전진
			ny = y+(dy[d]*i)
			nx = x+(dx[d]*i)
			if 0<=ny<n+1 and 0<=nx<m+1 and visit[ny][nx][d] == 0:
				if maps[ny][nx] == 0:
					visit[ny][nx][d] = 1
					queue.append((ny,nx,d,ins+1))
				elif maps[ny][nx] == 1:
					break
		for i in range(1,3):
			next_d = change_Dirs(d,i)
			if visit[y][x][next_d] == 0:
				visit[y][x][next_d] = 1
				queue.append((y,x,next_d,ins+1))

n,m = map(int,stdin.readline().split())

maps = [[1]*(m+1)]+[[1]+list(map(int,stdin.readline().split())) for _ in range(n)]
start_Y , start_X , start_dir = map(int,stdin.readline().split())
end_Y , end_X , end_dir = map(int,stdin.readline().split())
visit = [[[0 for _ in range(5)] for _ in range(m+1)] for _ in range(n+1)]
bfs(visit)
