from sys import stdin
n,m,s_x,s_y,k= map(int,stdin.readline().split())
board = [list(map(int,stdin.readline().split())) for _ in range(n)]
inst = list(map(int,stdin.readline().split()))
#클래스를 이용함 test
class Dice:
	def __init__(self,now_x,now_y,top,bottom,left,right,up,down):
		self.now_x = now_x
		self.now_y = now_y
		self.top = top
		self.bottom = bottom
		self.left = left
		self.right = right
		self.up = up
		self.down = down
# 초기값
dice= Dice(s_x,s_y,1,6,4,3,2,5)
dice_value = {1:0,2:0,3:0,4:0,5:0,6:0}
#1 동 /2 서 /3 북 /4 남
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def roll():
	for d in inst:
		nx = dice.now_x+dx[d-1]
		ny = dice.now_y+dy[d-1]
		if (0<=nx<n and 0<=ny<m):
			dice.now_x=nx
			dice.now_y=ny
			if d == 1:
				dice.top, dice.bottom, dice.left, dice.right = dice.left, dice.right, dice.bottom, dice.top
			elif d == 2:
				dice.top, dice.bottom, dice.left, dice.right = dice.right, dice.left, dice.top, dice.bottom
			elif d == 3:
				dice.top, dice.bottom, dice.up, dice.down = dice.down, dice.up, dice.top, dice.bottom
			elif d == 4:
				dice.top, dice.bottom, dice.up, dice.down = dice.up, dice.down, dice.bottom, dice.top

			if board[dice.now_x][dice.now_y] == 0:
				board[dice.now_x][dice.now_y] = dice_value[dice.bottom]
			else:
				dice_value[dice.bottom] = board[dice.now_x][dice.now_y]
				board[dice.now_x][dice.now_y] = 0
			print(dice_value[dice.top])
		else:
			continue

roll()