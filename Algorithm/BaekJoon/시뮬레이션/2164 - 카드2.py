from collections import deque
n = int(input())
q = deque([int(x) for x in range(1,n+1)])

while n!=1:
	q.popleft()
	q.rotate(-1)
	n-=1
print(q[0])