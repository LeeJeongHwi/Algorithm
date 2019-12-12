from sys import stdin
n = int(stdin.readline())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
	a,b = map(int,stdin.readline().split())
	# if a == 1:
	# 	tree[a].append(b)
	# elif b == 1:
	# 	tree[b].append(a)
	# else:
	# 	for i in tree:
	# 		if a in i:
	# 			tree[a].append(b)
	# 			break
	# 		elif b in i:
	# 			tree[b].append(a)
	# 			break
	tree[a].append(b)
	tree[b].append(a)
visit = [0 for _ in range(n+1)]
ans = [0 for _ in range(n+1)]

stack = []
def dfs(tree,ans,visit,start):
	stack.append(start)
	while stack:
		node = stack.pop()
		visit[node]=1
		for i in tree[node]:
			if not visit[i] :
				ans[i] = node
				stack.append(i)
dfs(tree,ans,visit,1)
for i in range(2,n+1):
	print(ans[i])