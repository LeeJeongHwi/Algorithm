from sys import stdin
import sys
from collections import deque
sys.setrecursionlimit(10**8)
def turn(d,ins):
	if d==1:
		if ins=='D':
			d=4
		else:
			d=3
	elif d==2:
		if ins=='D':
			d=3
		else:
			d=4
	elif d==3:
		if ins=='D':
			d=1
		else:
			d=2
	elif d==4:
		if ins=='D':
			d=2
		else:
			d=1
	return d
# While 문으로 바꾸면 좀 더 빠름
def movement(head,insNum,q):
	global second,d
	head[1] += dx[d]
	head[0] += dy[d]
	if (0<=head[0]<n and 0<=head[1]<n) and (board[head[0]][head[1]] != 2):
		if board[head[0]][head[1]]==1:
			board[head[0]][head[1]]=2
		else:
			y,x= q.popleft() #꼬리자름
			board[y][x] = 0 
		q.append([head[0],head[1]])
		board[head[0]][head[1]] = 2
		second+=1
		if insNum < ins:
			if second == int(inst[insNum][0]) :
				d= turn(d,inst[insNum][1])
				return movement(head,insNum+1,q)
		return movement(head,insNum,q)
	else:
		return

if __name__ == "__main__":

	n = int(stdin.readline())
	board = [[0]*(n) for _ in range(n)]
	apple = int(stdin.readline())
	for _ in range(apple):
		y,x = map(int,stdin.readline().split())
		board[y-1][x-1] = 1
	ins=int(stdin.readline())
	inst = [tuple(stdin.readline().rstrip().split()) for _ in range(ins)]
	#동 서 북 남
	dx=[0,1,-1,0,0]
	dy=[0,0,0,-1,1]
	second = 0
	head,tail,d=[0,0],[0,0],1
	q=deque([[0,0]])
	movement(head,0,q)
	second+=1

	print(second)
