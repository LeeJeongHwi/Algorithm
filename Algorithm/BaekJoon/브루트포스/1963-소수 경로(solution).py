"""
Solution : https://dyndy.tistory.com/216
"""
from sys import stdin
from collections import deque

t = int(stdin.readline())

#에라토스테네스의 체==================
def prime(n,pri):
	max_length = int(n**0.5)
	for i in range(2,max_length):
		if pri[i]:
			for j in range(i+i,n+1,i):
				if pri[j] is not False:
					pri[j] = False
pri = [True for _ in range(10000)]
prime(9999,pri)
#===================================

def bfs(now,visit):
	queue = deque()
	queue.append(now)
	visit[now] = 0
	while queue:
		node = queue.popleft()
		temp_node = node
		n1 = (temp_node // 1000) * 1000
		n2 = ((temp_node % 1000)//100) * 100
		n3 = ((temp_node % 100)//10) * 10
		n4 = (temp_node % 10)
		for i in range(0,10):
			if (visit[n1+n2+n3+i] == -1) and (pri[n1+n2+n3+i] is True):
				visit[n1+n2+n3+i] = visit[node]+1
				queue.append(n1+n2+n3+i)				
			if (visit[n1+n2+(i*10)+n4] == -1) and (pri[n1+n2+(i*10)+n4] is True):
				visit[n1+n2+(i*10)+n4] = visit[node] + 1
				queue.append(n1+n2+(i*10)+n4)
			if (visit[n1+(i*100)+n3+n4] == -1) and (pri[n1+(i*100)+n3+n4] is True):
				visit[n1+(i*100)+n3+n4] = visit[node] + 1
				queue.append(n1+(i*100)+n3+n4)
			if i==0:
				continue
			if (visit[(i*1000)+n2+n3+n4] == -1) and (pri[(i*1000)+n2+n3+n4] is True):
				visit[(i*1000)+n2+n3+n4] = visit[node] + 1
				queue.append((i*1000)+n2+n3+n4)
for i in range(t):
	now,new = map(int,stdin.readline().split())
	visit = [-1 for _ in range(10000)]
	if now == new:
		print(0)
		continue
	bfs(now,visit)
	if visit[new] == -1:
		print("Impossible")
	else:
		print(visit[new])
