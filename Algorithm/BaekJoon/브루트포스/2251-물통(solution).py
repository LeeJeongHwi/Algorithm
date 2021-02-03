"""
Solution : https://rebas.kr/769
"""
from sys import stdin
from collections import deque

a,b,c = map(int,stdin.readline().split())
visit = [[0]*201 for _ in range(201)]
q = deque()
ans = []
def check(x,y):
	if not visit[x][y]:
		visit[x][y] = 1
		q.append((x,y))

def bfs():
	q.append((0,0))
	visit[0][0] = 1
	while q:
		x,y = q.popleft() #X와 Y는 현재 A컵 B컵에 있는 물의 양
		z = c-x-y # C컵크기 - A,B에 있는 모든 물의양 = C컵에 남아있는 물의 양
		if not x:
			ans.append(z)
		#b-y,c-z,a-x ==> 들어갈 수 있는 물의 양 / x,y,z = 옮기려는 양 
		water = min(x,b-y) # x = 0 / b-y = 9  ==> water == 0
		check(x-water,y+water) # A컵 -> B컵
		
		water = min(x,c-z) # x = 0 / c-z = 0 ==> water == 0
		check(x-water , y) # A컵 -> C컵
		
		water = min(y,a-x) # y = 0 / a-x = 8 ==> water == 0
		check(x+water, y-water) #B컵 -> A컵

		water = min(y,c-z) # y = 0 / c-z = 0 ==> water == 0
		check(x,y-water) #B컵 -> C컵

		water = min(z,a-x) # z = 10 / a-x = 8 ==> water == 8
		check(x+water , y) #C컵 -> A컵

		water = min(z,b-y) # z = 10 / b-y = 9 ==> water == 9
		check(x,y+water) #C컵 -> B컵
bfs()
print(' '.join(map(str,sorted(ans))))

