from sys import stdin

n = int(input())

matrix = [list(stdin.readline().rstrip()) for _ in range(n)]
	
ans = 0

def checkUpDown(row,col): #해당하는 세로 라인 검사
	result = 1
	candy=1
	for j in range(n-1):
		if matrix[j][row] == matrix[j+1][row]:
			candy += 1
		else:
			result = max(result,candy)
			candy = 1
	result = max(result,candy)
	return result 


def checkLeftRight(row,col): #해당하는 가로 라인 검사
	result = 1
	candy = 1
	for j in range(n-1):
		if matrix[row][j] == matrix[row][j+1]:
			candy += 1
		else:
			result = max(result,candy)
			candy = 1
	result = max(result,candy)
	return result

for i in range(n):
	for j in range(n):
		#swap 후 line 검사
		if 0<=j+1<n:
			#왼쪽 사탕과 바꾸기
			matrix[i][j],matrix[i][j+1] = matrix[i][j+1],matrix[i][j]
			ans = max(ans,checkUpDown(i,j),checkLeftRight(i,j))
			ans = max(ans,checkUpDown(i,j+1),checkLeftRight(i,j+1))
			matrix[i][j],matrix[i][j+1] = matrix[i][j+1],matrix[i][j]
			#아래 사탕과 바꾸기
			matrix[j][i],matrix[j+1][i] = matrix[j+1][i],matrix[j][i]
			ans = max(ans,checkUpDown(j,i),checkLeftRight(j,i))
			ans = max(ans,checkUpDown(j+1,i),checkLeftRight(j+1,i))
			matrix[j][i],matrix[j+1][i] = matrix[j+1][i],matrix[j][i]
			
print(ans)