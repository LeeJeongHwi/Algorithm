from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
n,l,r = map(int,stdin.readline().split())
maps = [list(map(int,stdin.readline().split())) for _ in range(n)]
flag = False
count = 0

def movePeople(union):
	unionLen = len(union)
	if unionLen == 1:
		return
	unionSum = 0
	for y,x in union:
		unionSum+=maps[y][x]
	people = unionSum//unionLen
	for y,x in union:
		maps[y][x] = people
def setUnion(i,j,visit,unionNum):
	global flag
	union = [(i,j)]
	stack = [(i,j)]
	visit[i][j] = unionNum
	while stack:
		y,x = stack.pop()
		for dy,dx in [(0,1),(1,0),(-1,0),(0,-1)]:
			ny = dy+y
			nx = dx+x
			if 0<=ny<n and 0<=nx<n and visit[ny][nx] == 0:
				if (l<= abs(maps[y][x] - maps[ny][nx]) <= r): #연합이 이루어짐 (인구이동이 이루어짐)
					flag = True
					stack.append((ny,nx))
					visit[ny][nx] = unionNum
					union.append((ny,nx))
	movePeople(union)
def checkUnion():
	global flag,count
	visit = [[0 for _ in range(n)] for _ in range(n)]
	unionNum = 1
	for i in range(n):
		for j in range(n):
			if visit[i][j] == 0:
				setUnion(i,j,visit,unionNum)
				unionNum+=1
	if flag:
		count+=1
		flag = False
		return checkUnion()
	elif not flag:
		print(count)
		return
checkUnion()