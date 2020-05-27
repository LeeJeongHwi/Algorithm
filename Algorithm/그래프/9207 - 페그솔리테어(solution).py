# solution : https://boomrabbit.tistory.com/3
from sys import stdin,setrecursionlimit
setrecursionlimit(10**8)

n = int(stdin.readline())
dy = [1,-1,0,0]
dx = [0,0,1,-1]

def back(curmaps,count):
	global ans2
	for y in range(5):
		for x in range(9):
			if curmaps[y][x] == 'o':
				for i in range(4):
					ny=y+dy[i]
					nx=x+dx[i]
					if (0<=ny<5 and 0<=nx<9 and curmaps[ny][nx]=='o'):
						ny2=ny+dy[i]
						nx2=nx+dx[i]
						if (0<=ny2<5 and 0<=nx2<9 and curmaps[ny2][nx2]=='.'):
							curmaps[y][x]='.'
							curmaps[ny][nx] ='.'
							curmaps[ny2][nx2] = 'o'
							back(curmaps,count+1)
							curmaps[y][x]='o'
							curmaps[ny][nx] ='o'
							curmaps[ny2][nx2] = '.'
	ans2 = max(ans2,count)
	return
for t in range(n):
	maps = [list(stdin.readline().rstrip()) for _ in range(5)]
	ans1=0 
	for i in range(5):
		for j in range(9):
			if maps[i][j] == 'o':
				ans1+=1
	ans2=0
	back(maps,0)
	#최소 핀의 갯수는 f_pin - 이동횟수
	if t == n-1:
		pass
	else:
		blank = input()
	print(ans1-ans2,ans2)