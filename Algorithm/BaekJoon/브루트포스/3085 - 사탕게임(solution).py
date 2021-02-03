#solution : https://github.com/happiness96
from sys import stdin

n = int(input())

maps = [list(stdin.readline().rstrip()) for _ in range(n)]
	
result = 0

def count(row,col,color):
	global result
	#check Row
	# for i in maps:
	# 	print(i)
	candy = 0
	for i in range(row+1,n):
		if maps[col][i] == color:
			candy+=1
		else:
			break
	for i in range(row,-1,-1):
		if maps[col][i] == color:
			candy+=1
		else:
			break

	result = max(result,candy)
	#check col
	candy = 0 
	for i in range(col+1,n):
		if maps[i][row] == color:
			candy+=1
		else:
			break
	for i in range(col,-1,-1):
		if maps[i][row] == color:
			candy+=1
		else:
			break
	result = max(result,candy)
	# print(result)
	# print("===============")
		
def change():
	for i in range(n):
		for j in range(n):
			#change Row
			if 0<=j+1<n:
				maps[i][j],maps[i][j+1] = maps[i][j+1],maps[i][j]
				count(j,i,maps[i][j])
				count(j+1,i,maps[i][j+1])
				maps[i][j],maps[i][j+1] = maps[i][j+1],maps[i][j]
			#change Col
			if 0<=i+1<n:
				maps[i][j],maps[i+1][j] = maps[i+1][j],maps[i][j]
				count(j,i,maps[i][j])
				count(j,i+1,maps[i+1][j])
				maps[i][j],maps[i+1][j] = maps[i+1][j],maps[i][j]
change()
print(result)

#Python은 C++ 방식으로하면 시간초과가 난다.