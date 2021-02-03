n,m = map(int,input().split())

numlist = [i+1 for i in range(n)]
visit= [False] *n
ans=[]
j= 0 
def dfs(cnt,j):
	if cnt == m:
		print(*ans)
		return
	for i in range(j,n):
		if visit[i]:
			continue
		visit[i] = True
		ans.append(numlist[i])
		dfs(cnt+1,j+1)
		ans.pop()
		visit[i] = False
		j+=1
dfs(0,j)