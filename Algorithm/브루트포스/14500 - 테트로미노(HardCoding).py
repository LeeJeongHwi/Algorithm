from sys import stdin

n,m = map(int,stdin.readline().split())

board = [list(map(int,stdin.readline().split())) for _ in range(n)]

def Omino(i,j):
	omino = [[(i,j),(i+1,j),(i,j+1),(i+1,j+1)]]
	result = 0
	for line in omino:
		calc = 0
		flag = True 
		for y,x in line:
			if 0<=y<n and 0<=x<m:
				calc += board[y][x]
			else:
				flag = False
				break
		if flag:
			result = max(result,calc)
	return result

def Imino(i,j):
	imino = [[(i,j),(i+1,j),(i+2,j),(i+3,j)],
			  [(i,j),(i,j+1),(i,j+2),(i,j+3)]]
	result = 0
	for line in imino:
		calc = 0
		flag = True 
		for y,x in line:
			if 0<=y<n and 0<=x<m:
				calc += board[y][x]
			else:
				flag = False
				break
		if flag:
			result = max(result,calc)
	return result

def SZmino(i,j):
	szmino = [[(i,j),(i+1,j),(i+1,j+1),(i+2,j+1)],
			 [(i+1,j),(i,j+1),(i+1,j+1),(i,j+2)],
			 [(i,j),(i+1,j),(i+1,j-1),(i+2,j-1)],
			 [(i,j-1),(i,j-2),(i+1,j-1),(i+1,j)]]
	result = 0
	for line in szmino:
		calc = 0
		flag = True 
		for y,x in line:
			if 0<=y<n and 0<=x<m:
				calc += board[y][x]
			else:
				flag = False
				break
		if flag:
			result = max(result,calc)
	return result

def LJmino(i,j):
	ljmino = [[(i,j),(i+1,j),(i+2,j),(i+2,j+1)],
			 [(i,j),(i+1,j),(i,j+1),(i,j+2)],
			 [(i,j),(i,j+1),(i,j+2),(i-1,j+2)],
			 [(i,j),(i,j+1),(i+1,j+1),(i+2,j+1)],
			 [(i,j),(i+1,j),(i+2,j),(i+2,j-1)],
			 [(i,j),(i+1,j),(i,j-1),(i,j-2)],
			 [(i,j),(i,j-1),(i,j-2),(i-1,j-2)],
			 [(i,j),(i,j-1),(i+1,j-1),(i+2,j-1)]]
	result = 0
	for line in ljmino:
		calc = 0
		flag = True 
		for y,x in line:
			if 0<=y<n and 0<=x<m:
				calc += board[y][x]
			else:
				flag = False
				break
		if flag:
			result = max(result,calc)
	return result

def Tmino(i,j):
	tmino = [[(i,j),(i+1,j),(i,j+1),(i,j-1)],
			 [(i,j),(i-1,j),(i,j+1),(i,j-1)],
			 [(i,j),(i+1,j),(i-1,j),(i,j+1)],
			 [(i,j),(i+1,j),(i-1,j),(i,j-1)]]
	result = 0
	for line in tmino:
		calc = 0
		flag = True 
		for y,x in line:
			if 0<=y<n and 0<=x<m:
				calc += board[y][x]
			else:
				flag = False
				break
		if flag:
			result = max(result,calc)
	return result

maxNum = 0
for i in range(n):
	for j in range(m):
		maxNum = max(maxNum,Omino(i,j),Imino(i,j),SZmino(i,j),LJmino(i,j),Tmino(i,j))
print(maxNum)