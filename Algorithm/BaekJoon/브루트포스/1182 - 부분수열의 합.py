from sys import stdin
from itertools import combinations
n,s = map(int,stdin.readline().split())

num = list(map(int,stdin.readline().split()))

# visit = [False] * n

cnt = 0

# def dfs(idx,re):
# 	global cnt 
# 	for i in range(idx,n):
# 		if not visit[i]:
# 			visit[i] = True
# 			dfs(i,re+num[i])
# 			visit[i] = False
# dfs(0,0)
# print(cnt)

for i in range(1,n+1):
	for j in combinations(num,i):
		if sum(j) == s:
			cnt+=1
print(cnt)