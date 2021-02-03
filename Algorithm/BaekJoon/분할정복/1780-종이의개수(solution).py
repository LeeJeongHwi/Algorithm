"""
Solution : https://joosjuliet.github.io/1780/
"""
from sys import stdin
import sys
sys.setrecursionlimit(10**8)

n = int(stdin.readline())
m=n
matrix = [0 for _ in range(n)]
ans = [0]*3 # -1 0 1 순


for i in range(n):
	line = list(map(int,stdin.readline().split()))
	matrix[i] = line

def check(x,y,n):
	for i in range(x,x+n):
		for j in range(y,y+n):
			if matrix[x][y] != matrix[i][j]:
				return False
	return True

def solution(x,y,s): # s = 자른 종이의 개수 
	if check(x,y,s):
		ans[matrix[x][y]+1] += 1
		return #여기서 왜 Return 이 들어가있는가?
	#검사를 했을 때 -1,0,1 이 섞여 있을 때
	s //= 3
	for i in range(0,3):
		for j in range(0,3):
			print(x+i*s , y+j*s , s)
			solution(x+i*s,y+j*s,s)

solution(0,0,n)
for i in ans:
	print(i)