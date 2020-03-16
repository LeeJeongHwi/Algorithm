from sys import stdin

n,m = map(int,stdin.readline().split())

chessBoard = [[x for x in stdin.readline().rstrip()] for _ in range(n)]

newChess = [[0]*m for _ in range(n)]

def repaint(firstBlock,row,col):
	block = firstBlock
	count = 0
	for i in range(row, row+8):
		for j in range(col,col+8):
			if block == 'W':
				if block != chessBoard[i][j]:
					count+=1
				block = 'B'
			elif block == 'B':
				if block != chessBoard[i][j]:
					count+=1
				block = 'W'
		if block == 'W':
			block = 'B'
		else:
			block = 'W'
	return count

ans = 65
for row in range(0,n-7):
	for col in range(0,m-7):
		ans = min(repaint("W",row,col),repaint("B",row,col),ans)
print(ans)