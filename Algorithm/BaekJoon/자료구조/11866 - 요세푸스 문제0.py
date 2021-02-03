from collections import deque
from sys import stdin

n,k = map(int,stdin.readline().split())

q = deque([str(x) for x in range(1,n+1)])
rem = []

n = 1
while q:
	if n==k:
		rem.append(q.popleft())
		n=1
		continue
	q.append(q.popleft())
	n+=1
print('<'+', '.join(rem)+'>')