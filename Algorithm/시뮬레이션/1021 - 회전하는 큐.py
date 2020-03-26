from sys import stdin
import sys
from collections import deque
sys.setrecursionlimit(10**7)
size,count = map(int,stdin.readline().split())
queue = deque([int(x) for x in range(1,size+1)])
wantData = list(map(int,stdin.readline().split()))
c = 0
size-=1
#마찬가지로 While을 쓰면 좀 더 빠르게 나올 수 있음
def rotate(q,c,cnt):
	global size
	#0과 targetIndex, size와 targetIndex의 거리
	targetIndex = q.index(wantData[c])
	now = q[0]
	if now == wantData[c]:
		q.popleft()
		size-=1
		if c==count-1:
			print(cnt)
			return
		c+=1
		return rotate(q,c,cnt)
	elif (size-targetIndex) >= targetIndex:
		q.append(q.popleft())
		return rotate(q,c,cnt+1)
	else:
		q.appendleft(q.pop())
		return rotate(q,c,cnt+1)

rotate(queue,c,0)