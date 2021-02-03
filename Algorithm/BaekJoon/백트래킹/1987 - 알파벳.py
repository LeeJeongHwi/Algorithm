"""
BFS 로도 풀 수 있다 --> Python3 으로 통과 가능
BackTracking 자체가 python이 엄청 느리고,
pypy3으로 통과 시켜야함
"""
from sys import stdin
r,c = map(int,stdin.readline().split())
matrix = [list(stdin.readline().rstrip()) for _ in range(r)]
maxNum = 0
alpha = [False] * 26
def back(y,x,cnt):
	global maxNum,check
	if cnt >= maxNum:
		maxNum=cnt
	#4방향 탐색
	if 0<=y<r and 0<=x+1<c :
		if not alpha[ord(matrix[y][x+1])-ord('A')]:
			alpha[ord(matrix[y][x+1])-ord('A')]=True
			back(y,x+1,cnt+1)
			alpha[ord(matrix[y][x+1])-ord('A')]=False
	if 0<=y+1<r and 0<=x<c:
		if not alpha[ord(matrix[y+1][x])-ord('A')]:
			alpha[ord(matrix[y+1][x])-ord('A')]=True
			back(y+1,x,cnt+1)
			alpha[ord(matrix[y+1][x])-ord('A')]=False

	if 0<=y<r and 0<=x-1<c:
		if not alpha[ord(matrix[y][x-1])-ord('A')]:
			alpha[ord(matrix[y][x-1])-ord('A')]=True
			back(y,x-1,cnt+1)
			alpha[ord(matrix[y][x-1])-ord('A')]=False

	if 0<=y-1<r and 0<=x<c:
		if not alpha[ord(matrix[y-1][x])-ord('A')]:
			alpha[ord(matrix[y-1][x])-ord('A')]=True
			back(y-1,x,cnt+1)
			alpha[ord(matrix[y-1][x])-ord('A')]=False


alpha[ord(matrix[0][0]) - ord('A')] = True
back(0,0,1)
print(maxNum)