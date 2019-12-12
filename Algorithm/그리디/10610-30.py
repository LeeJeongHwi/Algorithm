from sys import stdin

def solution(n):
	if '0' not in n:
		return -1
	#30의 배수가 되는 조건
	if sum(map(int,n))%3==0:
		n.sort(reverse=True)
	else:
		return -1
	return n

n = [x for x in stdin.readline().rstrip()]
n = solution(n)
if n != -1:
	print("".join(n))
else:
	print(n)