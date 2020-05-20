from sys import stdin,setrecursionlimit
from collections import deque
setrecursionlimit(10**7)
n = int(stdin.readline())
maps = [list(map(int,stdin.readline().split())) for _ in range(n)]
size = 2
nowShark = 0
queue = deque()
result = 0
count =0
#초기 상어 위치
for i in range(n):
	for j in range(n):
		if maps[i][j] == 9:
			queue.append((i,j))
			nowShark= [i,j]
"""
물고기 먹는 기준
1. 거리
2. 가장 위(y값이 작음)
3. 가장 왼쪽(x값이 작음)
"""
def eatFish(canEat,i,j):
	global maps,result,count,size
	canEat.sort(key=lambda x:(x[2],x[0],x[1]))
	eat = canEat[0] #잡아먹을 물고기
	#상어 이동
	maps[i][j] = 0
	maps[eat[0]][eat[1]]=9
	result += eat[2]	
	count +=1
	#size 변환
	if size == count:
		size+=1
		count=0
	#상어 위치 수정
	nowShark[0],nowShark[1] = eat[0],eat[1]
	queue.append((eat[0],eat[1]))
def search_Fish(visit,i,j):
	canEat = []
	while queue:
		y,x = queue.popleft()
		for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]:
			ny = y+dy
			nx = x+dx
			if 0<=ny<n and 0<=nx<n and visit[ny][nx] == 0: 
				#먹을 수 있는 물고기 탐색
				if maps[ny][nx] == 0 or size == maps[ny][nx]:
					visit[ny][nx] = visit[y][x] + 1
					queue.append((ny,nx))
				elif size > maps[ny][nx]:
					visit[ny][nx] = visit[y][x] + 1
					canEat.append((ny,nx,visit[ny][nx]-1))
	if canEat:
		eatFish(canEat,i,j)
	else:
		return
while True:
	visit = [[0 for _ in range(n)] for _ in range(n)]
	if queue:
		visit[nowShark[0]][nowShark[1]] = 1
		search_Fish(visit,nowShark[0],nowShark[1])
	elif not queue:
		print(result)
		break