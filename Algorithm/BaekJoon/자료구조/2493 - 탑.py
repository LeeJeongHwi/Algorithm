from sys import stdin
from collections import deque
t = int(stdin.readline())

tower = list(map(int,stdin.readline().split()))

answer = ['0' for _ in range(t)]
stack = []
def laser(n):
	# print("N:",n,"tower[n]:",tower[n])
	# print("stack:",stack)
	while stack:
		if stack[-1][0] < tower[n]:
			answer[stack[-1][1]] = str(n+1)
			stack.pop()
		else:
			break

for i in range(t-1,-1,-1):
	laser(i)
	stack.append((tower[i],i))

print(' '.join(answer))