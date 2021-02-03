from sys import stdin
from collections import deque

t = int(stdin.readline())
def solve(q):
	#뒤집히면 False , 안뒤집히면 True
	global flag
	for c in func:
		if c =='R':
			flag=not flag
		elif c == 'D':
			if not q:
				print("error")
				return False
			elif flag:
				if q.popleft()=='':
					print("error")
					return False
			elif not flag:
				if q.pop()=='':
					print('error')
					return False
	return True
for _ in range(t):
	func = stdin.readline().rstrip()
	n = int(stdin.readline())
	a = deque(stdin.readline().rstrip().split(','))
	a[0] = a[0][1:]
	a[-1] = a[-1][:-1]
	# print(a)
	flag = True
	if solve(a):
		if flag:
			print("["+','.join(a)+']')	
		else:
			a.reverse()
			print("["+','.join(a)+']')

# pop 대신 인덱스를 쓰면 더 빠르다.