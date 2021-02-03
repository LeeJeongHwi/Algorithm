from sys import stdin
from collections import deque
t = int(stdin.readline())

def command_L(n):
	num = n//1000
	d1 = n%1000 * 10
	result = num+d1
	return result
def command_R(n):
	d4 = n%10
	num = n//10
	result = d4*1000+num
	return result


def bfs(A):
	queue = deque()
	queue.append((A,""))
	visit = [0 for _ in range(10000)]
	visit[A] = 1
	while queue:
		n,command = queue.popleft()
		if n == B:
			print(command)
			return
		#command D
		if 2*n > 9999:
			if visit[2*n%10000] == 0:
				visit[2*n%10000] = 1
				D = command+"D"
				queue.append((2*n%10000,D))
		else:
			if visit[2*n] == 0:
				visit[2*n] = 1
				D = command + "D"
				queue.append((2*n,D))
		#command S
		if n == 0:
			if visit[9999] == 0 :
				visit[9999] = 1
				S = command+"S"
				queue.append((9999,S))
		else:
			if visit[n-1] == 0:
				visit[n-1] = 1
				S = command + "S"
				queue.append((n-1,S))
		#command L
		resultL = command_L(n)
		if visit[resultL] == 0:
			visit[resultL] = 1
			L = command+"L"
			queue.append((resultL,L))		
		#command R
		resultR = command_R(n)
		if visit[resultR] == 0:
			visit[resultR] = 1
			R = command+"R"
			queue.append((resultR,R))

for _ in range(t):
	A,B = map(int,stdin.readline().split())
	bfs(A)
