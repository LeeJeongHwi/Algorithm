n,m = map(int,input().split())

numlist = [i+1 for i in range(n)]
ans=[]
def dfs(cnt,j):
	if cnt == m:
		print(*ans)
		return
	for i in range(j,n):
		ans.append(numlist[i])
		dfs(cnt+1,j)
		ans.pop()
		j+=1
dfs(0,0)
