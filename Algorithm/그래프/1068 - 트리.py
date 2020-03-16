from sys import stdin

n = int(stdin.readline())

tree = [int(x) for x in stdin.readline().rstrip().split()]

rm_node = int(stdin.readline())

graph = [[]*n for _ in range(n)]

root_node = 0

for i,node in enumerate(tree):
	if node == -1:
		root_node = i
		continue
	if rm_node == i:
		continue
	if node == rm_node:
		continue
	graph[node].append(i)

def dfs(start):
	count = 0
	stack = []
	visit = [0 for _ in range(n)]
	stack.append(start)
	#탐색 제거
	while stack:
		nd = stack.pop()
		visit[nd]= 1
		if not graph[nd]:
			count +=1
		else:
			for node in graph[nd]:
				if rm_node == node:
					graph[nd] = []
					continue
				if visit[node] == 0:
					stack.append(node)
	return count
if root_node == rm_node:
	print(0)
else:
	print(dfs(root_node))