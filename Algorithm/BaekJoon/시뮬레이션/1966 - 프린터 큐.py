from sys import stdin
from collections import deque
t = int(stdin.readline())

def solve(n,target,queue):
	cnt = 0
	while True:
		maxP = max(queue,key=lambda x:x[1])[1]
		node = queue.popleft()
		if node[1] == maxP:
			cnt+=1
			if node[0] == target:
				return cnt
		else:
			queue.append(node)

for _ in range(t):
	n,target = map(int,stdin.readline().split())
	queue = deque()
	for index,weight in enumerate(list(map(int,stdin.readline().split()))):
		#(target, weight) = (0,1),(1,2),(2,3),(3,4) 
		queue.append([index,weight])
	print(solve(n,target,queue))
