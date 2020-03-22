n,m = map(int,input().split())

numlist = [i+1 for i in range(n)]
ans=[]
def dfs(cnt):
	if cnt == m:
		print(*ans)
		return
	for i in range(n):
		ans.append(numlist[i])
		dfs(cnt+1)
		ans.pop()
dfs(0)

#iterTools.product를 써도 가능!