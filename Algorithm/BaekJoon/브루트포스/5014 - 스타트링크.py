# 강호 S층
# 총 F층 / G층으로 이동 / U는 위로 U층을 가는 버튼 / D는 아래로로 D층 가는 버튼
from sys import stdin
from collections import deque

f,s,g,u,d = map(int,stdin.readline().split())
visit = [-1 for _ in range(f+1)]
visit[s] = 0
button = [u,-d]

queue = deque()

def bfs(start):
	queue.append(start)

	while queue:
		nowFloor = queue.popleft()
		if nowFloor == g:
			print(visit[g])
			return
		for i in range(2):
			nextFloor = nowFloor + button[i]
			if (nextFloor <= f) and (nextFloor > 0) and visit[nextFloor] == -1:
				visit[nextFloor] = visit[nowFloor] + 1
				queue.append(nextFloor)
	print('use the stairs')
bfs(s)