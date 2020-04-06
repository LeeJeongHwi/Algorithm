from sys import stdin

n = int(stdin.readline())

cons = [list(map(int,stdin.readline().split())) for _ in range(n)]

visit = [False]*n

ans = 0
#Back Tracking
def dfs(day,money):
	global ans
	# print(visit)
	if ans <= money:
		ans = money
	for i in range(day,n):
		if i+cons[i][0] <= n and not visit[i]:
			visit[i] = True
			dfs(i+cons[i][0],money+cons[i][1])
			visit[i] = False
dfs(0,0)
print(ans)