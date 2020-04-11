#solution : https://inspirit941.tistory.com/entry/Python-백준-15683-감시
#시간을 더 단축 시킬 수 있으나 ...지금 머리로는 힘듬..
from sys import stdin
import copy
n,m = map(int,stdin.readline().split())

office = [list(map(int,stdin.readline().split())) for _ in range(n)]

cctv = []
for i in range(n):
	for j in range(m):
		if office[i][j] != 0 and office[i][j] != 6:
			cctv.append((i,j,office[i][j]))

tvNum = len(cctv)
#0 동 1 남  2 서 3 북
direction = {1:[[0],[1],[2],[3]],
			 2:[(0,2),(1,3)],
			 3:[(0,1),(1,2),(2,3),(3,0)],
			 4:[(0,1,2),(1,2,3),(2,3,0),(3,0,1)],
			 5:[(0,1,2,3)]}
minCount = float("inf")

def search(maps,y,x,direct):
	maps = copy.deepcopy(maps)
	for dirs in direct:
		if dirs == 0:
			for dx in range(x,m):
				if maps[y][dx] == 6:
					break
				elif maps[y][dx] != 0:
					continue
				else:
					maps[y][dx] = '#'
		elif dirs == 1:		
			for dy in range(y,n):
				if maps[dy][x] == 6:
					break
				elif maps[dy][x] != 0:
					continue
				else:
					maps[dy][x] = '#'

		elif dirs == 2:
			for dx in range(x,-1,-1):
				if maps[y][dx] == 6:
					break
				elif maps[y][dx] != 0:
					continue
				else:
					maps[y][dx] = '#'

		elif dirs == 3:
			for dy in range(y,-1,-1):
				if maps[dy][x] == 6:
					break
				elif maps[dy][x] != 0:
					continue
				else:
					maps[dy][x] = '#'
	return maps
def check(maps):
	zeroCount = 0
	for i in maps:
		zeroCount += i.count(0)
	# 	print(i)
	# print("ZERO COUNT :",zeroCount)
	# print("=============")
	return zeroCount


def backT(idx,maps):
	global minCount
	if idx == tvNum:
		zero = check(maps)
		minCount = min(minCount,zero)
		return
	y,x,tv = cctv[idx]
	direct = direction[tv]
	for i in direct:
		next_maps = search(maps,y,x,i)
		backT(idx+1,next_maps)
backT(0,office)
print(minCount)