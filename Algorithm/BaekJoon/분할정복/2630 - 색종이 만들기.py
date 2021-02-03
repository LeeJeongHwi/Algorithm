from sys import stdin
n = int(stdin.readline())

paper = [list(map(int,stdin.readline().split())) for _ in range(n)]

ans = [0,0]

def check(y,x,n):
	for i in range(y,y+n):
		for j in range(x,x+n):
			if paper[y][x] != paper[i][j]:
				return False
	return True

def solution (y,x,s):
	if check(y,x,s):
		ans[paper[y][x]] += 1
		return
	s//=2
	for i in range(0,2):
		for j in range(0,2):
			solution(y+i*s,x+j*s,s)
solution(0,0,n)
for a in ans:
	print(a)