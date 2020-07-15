from sys import stdin

n_s = int(input())
sinker = list(map(int,stdin.readline().split()))
n_m = int(input())
marble = list(map(int,stdin.readline().split()))
ans = []
visit = [[0 for _ in range(sum(sinker)+1)] for _ in range(n_s+1)]
def dfs(sinker,n_s,now,left,right,visit):
	new = abs(left-right)
	if new not in ans:
		ans.append(new)
	if now == n_s:
		return 0
	if (visit[now][new] == 0):
		dfs(sinker,n_s,now+1,left+sinker[now],right,visit)

		dfs(sinker,n_s,now+1,left,right+sinker[now],visit)

		dfs(sinker,n_s,now+1,left,right,visit)

		visit[now][new] = 1

dfs(sinker,n_s,0,0,0,visit)

# for i in visit:
# 	print(i)

# print(ans)

for i in range(n_m):
	if marble[i] in ans:
		print("Y", end=' ')
	else:
		print("N", end=' ')


