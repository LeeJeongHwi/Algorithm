from sys import stdin
from itertools import permutations
n,m = map(int,stdin.readline().split())

numlist = [x for x in range(1,n+1)]
visit = [False]*n
ans = []
def dfs(cnt):
	if cnt == m:
		print(*ans)
		return
	for i in range(0,n):
		if visit[i]:
			#방문 했다는 의미
			continue

		visit[i] = True
		ans.append(numlist[i])
		dfs(cnt+1)
		print(ans)
		ans.pop()
		visit[i] = False
dfs(0)