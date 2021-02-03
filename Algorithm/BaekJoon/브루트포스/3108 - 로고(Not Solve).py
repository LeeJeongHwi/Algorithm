from sys import stdin
from collections import deque
class rec:
	x1,y1 = 0,0
	x2,y2 = 0,0

	def __init__(self,x1,x2,y1,y2): #생성자
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2

n = int(stdin.readline())

recList = []
judge = 0
cnt = 0
visit = [0 for _ in range(n+1)]
q = deque()

def isOverlap(n,c): #a는 새로운것 b는 기존 것
	#기존의 것이 포함될 때 
	if (n.x1 < c.x1) and (n.y1 < c.y1) and (n.x2 > c.x2) and (n.y2 > c.y2):
		return False
	#새로운 것이 포함될 때
	if (n.x1 > c.x1) and (n.y1 > c.y1) and (n.x2 < c.x2) and (n.y2 < c.y2):
		return False
	if (c.x2 < n.x1) or (c.x1 > n.x2) or (c.y2 < n.y1) or (c.y1 > n.y2):
	#이해 안됨
		return False
	return True
def bfs():
	while q:
		now = q.popleft()
		for i in range(n):
			if visit[i] :
				continue
			if isOverlap(recList[i] , now):
				visit[i] = 1
				q.append(recList[i])

# recList.append(rec(0,0,0,0))

for i in range(n):
	x1,y1,x2,y2 = map(int,stdin.readline().split())
	recList.append(rec(x1,x2,y1,y2))
	if ((x1,y1) == (0,0)) or ((x2,y2) == (0,0)) or ((x1,y2) == (0,0)) or ((x2,y1) == (0,0)):
		judge = 1

for i in range(n):
	if not visit[i]:
		q.append(recList[i])
		visit[i] = 1
		bfs()
		cnt+=1
if judge == 1:
	cnt -=1
print(cnt)

