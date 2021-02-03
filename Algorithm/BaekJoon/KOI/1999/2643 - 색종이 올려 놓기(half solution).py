#solution : https://redsalmon.tistory.com/33
from sys import stdin
#색종이는 맨 위로 올린다. (큰 순서대로 올린다.)
n = int(input())
papers = [list(map(int,stdin.readline().split())) for _ in range(n)]
for i in range(n):
	papers[i].append(papers[i][0]*papers[i][1])
papers.sort(reverse=True,key=lambda x: x[2])
# print(papers)
dp = [0 for _ in range(n)]

def comp(i,j):
	# print(papers[i][0],papers[i][1],"가볍게 얘기할게 아니에요",papers[j][0],papers[j][1])
	if papers[i][0] >= papers[j][0] and papers[i][1] >= papers[j][1]:
		return True
	elif papers[i][0] >= papers[j][1] and papers[i][1] >= papers[j][0]:
		return True
	return False
ans = 0
for i in range(n):
	for j in range(i):
		if comp(j,i) and dp[i] < dp[j]:
			dp[i] = dp[j]
	dp[i]+=1
	ans = max(dp[i],ans) #이거 왜들어감?

print(ans)



""" dfs방식(백트래킹)은 시간초과가 일어난다.
def dfs(index,visit,count):
	global max_count,papers
	if index == n-1:
		if max_count < count :
			max_count = count
			# print(visit)
		return
	for i in range(index+1,n):
		if papers[index][0] >= papers[i][0] and papers[index][1] >= papers[i][1]:
			visit[i] = True
			dfs(i,visit,count+1)
			visit[i] = False
		elif papers[index][0] >= papers[i][1] and papers[index][1] >= papers[i][0]:
			visit[i] = True
			papers[i][0],papers[i][1] = papers[i][1],papers[i][0]
			dfs(i,visit,count+1)
			papers[i][0],papers[i][1] = papers[i][1],papers[i][0]
			visit[i] = False
# print(papers)
for i in range(n):
	visit = [False for _ in range(n)]
	visit[i] = True
	dfs(i,visit,1)
print(max_count)
"""