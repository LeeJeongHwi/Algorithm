#solution : https://chldkato.tistory.com/37
from sys import stdin
from collections import deque

def monkey(y,x,z):
	for dy,dx in [(1,0),(-1,0),(0,-1),(0,1)]:
		ny = y+dy
		nx = x+dx
		if 0<=ny<h and 0<=nx<w and visit[ny][nx][z] == 0:
			if maps[ny][nx] == 0:
				visit[ny][nx][z] = visit[y][x][z] + 1
				queue.append((ny,nx,z))
def horse(y,x,z):
	for dy,dx in [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]:
		ny = y+dy
		nx = x+dx
		if 0<=ny<h and 0<=nx<w and visit[ny][nx][z+1] == 0:
			if maps[ny][nx] == 0:
				visit[ny][nx][z+1] = visit[y][x][z]+1
				queue.append((ny,nx,z+1))

def bfs(k,visit):
	queue.append((0,0,0))
	visit[0][0][0] = 1
	while queue:
		y,x,z = queue.popleft()
		if y == h-1 and x == w-1:
			print(visit[y][x][z]-1)
			return		
		if z < k: #횟수가 남아 있을 때
			horse(y,x,z)
			monkey(y,x,z)
		elif z == k: #횟수가 없을 때 
			monkey(y,x,z)
	print(-1)

if __name__ == "__main__":
	k = int(stdin.readline())
	w,h = map(int,stdin.readline().split())
	maps = [list(map(int,stdin.readline().split())) for _ in range(h)]
	visit = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]
	queue = deque()
	bfs(k,visit)
	for i in visit:
		print(i)