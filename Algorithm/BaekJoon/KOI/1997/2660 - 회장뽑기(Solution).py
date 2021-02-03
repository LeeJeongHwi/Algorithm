#solution : https://it-garden.tistory.com/302
from sys import stdin
n = int(input())

member = [[float('inf') for _ in range(n)] for _ in range(n)]
while True:
	a,b = map(int,stdin.readline().split())
	if a == -1 and b == -1:
		break
	member[a-1][b-1] = 1
	member[b-1][a-1] = 1

for i in range(n):
	member[i][i] = 0

for k in range(n):
	for i in range(n):
		for j in range(n):
			if member[i][j] > member[i][k]+member[k][j]:
				member[i][j] = member[i][k]+member[k][j]
ans = []
for i in range(n):
	ans.append(max(member[i]))
min_point = min(ans)
print(min_point,ans.count(min_point))
for i,m in enumerate(ans):
	if m == min_point:
		print(i+1,end=' ')

# BFS로 다시풀어보기