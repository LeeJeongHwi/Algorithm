from collections import deque
from sys import stdin

q = deque()
n = int(stdin.readline())
for i in range(n):
	inst = list(stdin.readline().rstrip().split())
	if inst[0] == 'push':
		q.append(inst[1])
	elif inst[0] == 'pop':
		if not q:
			print(-1)
			continue
		print(q.popleft())
	elif inst[0] == 'size':
		print(len(q))
	elif inst[0] == 'empty':
		if not q:
			print(1)
		else:
			print(0)
	elif inst[0] == 'front':
		if not q:
			print(-1)
			continue
		print(q[0])
	elif inst[0] == 'back':
		if not q:
			print(-1)
			continue
		print(q[-1])
#len 을 안쓰면 좀 더 시간절약 가능