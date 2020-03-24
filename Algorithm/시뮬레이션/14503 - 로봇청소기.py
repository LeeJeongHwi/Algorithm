from sys import stdin

#input
n , m = map(int,stdin.readline().split())
r,c,di = map(int,stdin.readline().split())
#d == 0 (북쪽) / 1 (동쪽) / 2(남쪽) / 3 (서쪽)
board = [list(map(int,stdin.readline().split())) for _ in range(n)]
#북 동 남 서
dx = [0,1,0,-1]
dy = [-1,0,1,0]
cnt = 1
def dfs(y,x,d):
	global cnt
	board[y][x] = 2
	#반시계방향으로 4방향 탐색
	for i in range(4):
		next_d = ((d+(4-i)+3)%4)
		nx = x+dx[next_d]
		ny = y+dy[next_d]
		if (0<=ny<n and 0<=nx<m):
			if board[ny][nx] != 0:
				continue
			cnt+=1
			return dfs(ny,nx,next_d)
	
	#4방향 다 갈 곳이 없다
	back_d = (d+2)%4
	nx = x+dx[back_d]
	ny = y+dy[back_d]
	if board[ny][nx] == 1:
		return
	return dfs(ny,nx,d)

dfs(r,c,di)
print(cnt)

