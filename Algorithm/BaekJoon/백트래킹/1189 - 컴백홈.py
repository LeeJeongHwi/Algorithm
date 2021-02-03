from sys import stdin

r,c,k = map(int,stdin.readline().split())

maps = [list(stdin.readline().rstrip()) for _ in range(r)]
visit = [[False]*c for _ in range(r)]
#시작 장소 - (r-1,0) / 도착장소 - (0,c-1)

result = 0
def dfs(y,x,cnt):
	global result,visit
	if y == 0 and x == c-1:
		if cnt == k:
			result+=1
			return

	if 0<=y<r and 0<=x+1<c :
		if maps[y][x+1] == '.' and not visit[y][x+1]:
			visit[y][x+1]=True
			dfs(y,x+1,cnt+1)
			visit[y][x+1]=False
	if 0<=y+1<r and 0<=x<c:
		if maps[y+1][x] == '.' and not visit[y+1][x]:
			visit[y+1][x]=True
			dfs(y+1,x,cnt+1)
			visit[y+1][x]=False

	if 0<=y<r and 0<=x-1<c:
		if maps[y][x-1] == '.' and not visit[y][x-1]:
			visit[y][x-1]=True
			dfs(y,x-1,cnt+1)
			visit[y][x-1]=False

	if 0<=y-1<r and 0<=x<c:
		if maps[y-1][x] == '.' and not visit[y-1][x]:
			visit[y-1][x]=True
			dfs(y-1,x,cnt+1)
			visit[y-1][x]=False
visit[r-1][0] = True
dfs(r-1,0,1)
print(result)