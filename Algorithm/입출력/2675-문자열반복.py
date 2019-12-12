from sys import stdin

T=int(input())
for i in range(T):
	R,S = stdin.readline().split()
	for j in S:
		print(j*int(R),end='')
	print()

#다른 사람 풀이 == 내 풀이 