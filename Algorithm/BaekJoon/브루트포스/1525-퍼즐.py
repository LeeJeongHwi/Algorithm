"""
Solution : https://scarletbreeze.github.io/articles/2019-08/BOJ(%EB%AC%BC%ED%86%B5)
"""
from sys import stdin
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1] 
matrix = [list(map(int,stdin.readline().split())) for _ in range(3)]
start = 0
for i in range(3):
	for j in range(3):
		if matrix[i][j] == 0:
			matrix[i][j] = 9
		start = start*10 + matrix[i][j] #xxxxxxxxx 형태로 만들기 위함
def bfs():
	queue = deque()
	queue.append(start)
	while queue:
		now_num = queue.popleft() #9자리 정수
		now = str(now_num)
		z = now.find('9')
		x = z//3 #ex) z == 1 x = 1//3 and y = 1%3 => (0,1) 
		y = z%3
		for i in range(4):
			nx,ny = x+dx[i] , y+dy[i]
			if 0<= nx < 3 and 0 <= ny < 3:
				temp = list(now)
				temp[x*3+y],temp[nx*3+ny] = temp[nx*3+ny],temp[x*3+y]
				#여기를 어떻게 생각해!!!!!!!! 이해는 되었다만!!!!
				chg_num = int(''.join(temp))

				# print("바뀌기 전 Matrix :",now)
				# print("바뀐 Matrix :",chg_num)
				# print("===========================")
				
				if chg_num not in dist:
					dist[chg_num] = dist[now_num] + 1
					queue.append(chg_num)

dist={}
dist[start] = 0
bfs()
if 123456789 in dist:
	print(dist[123456789])
else:
	print(-1)