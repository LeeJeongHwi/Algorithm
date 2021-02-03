#solution : http://jaegualgo.blogspot.com/2017/07/boj-2876.html
#솔직히 이거는 문제를 이해하기가 더 어려웠다.
from sys import stdin
n = int(stdin.readline())
A = []
B = []

for _ in range(n):
	ai,bi = map(int,stdin.readline().split())
	A.append(ai)
	B.append(bi)

min_g = 0;
max_l = -1;
for g in range(1,6):
	l = 0
	for i in range(n):
		if g==A[i] or g == B[i]:
			l+=1
		else:
			l = 0
		if l > max_l:
			max_l = l
			min_g = g
print(max_l,min_g)