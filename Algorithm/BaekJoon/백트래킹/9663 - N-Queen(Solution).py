# solution : https://rebas.kr/761
n = int(input()) #2n-1 인 이유를 모르겠음
row,dia_R,dia_L = [False]*n,[False]*(2*n-1),[False]*(2*n-1) 
count = 0
def dfs(x):
	global count
	if x==n:
		count+=1
		return
	for i in range(n):
		if not (row[i] or dia_R[x+i] or dia_L[x-i+n-1]):
			row[i] = dia_R[x+i] = dia_L[x-i+n-1] = True
			dfs(x+1)
			row[i] = dia_R[x+i] = dia_L[x-i+n-1] = False
			
dfs(0)
print(count)

""" 내가 짠 코드 - 메모리초과
chess = [[0]*n for _ in range(n)]
count = 0
def checking(y,x,chess):
	#세로 Check
	for col in range(y-1,-1,-1):
		if chess[col][x]:
			return False

	# #오른쪽 위 대각선
	for i in range(1,n):
		if 0<=y-i<n and 0<=x+i<n:
			if chess[y-i][x+i]:
				return False
		else:
			break
	#왼쪽 위 대각선
	for i in range(1,n):
		if 0<=y-i<n and 0<=x-i<n:
			if chess[y-i][x-i]:
				return False
		else:
			break
	return True


def back(y,x,chess):
	global count
	if y == n:
		count+=1
		return
		
	for row in range(n):
		chess[y][row] = 1
		if checking(y,row,chess):
			back(y+1,row,chess)
		chess[y][row] = 0


back(0,0,chess)
print(count)
"""