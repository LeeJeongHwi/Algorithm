from sys import stdin
from collections import deque
v = int(stdin.readline())
tree = [[] for _ in range(v+1)]

def bfs(tree,start):
	visit = [0 for _ in range(v+1)]
	queue = deque()
	queue.append((start,0))
	visit[start] = 1
	deepNode = (start,0)
	while queue:
		nowNode = queue.popleft()
		if nowNode[1] > deepNode[1]:
			deepNode = nowNode
		for nextNode in tree[nowNode[0]]:
			if not visit[nextNode[0]]: #다음에 방문할 노드가 방문안했다면 
				visit[nextNode[0]] = 1
				queue.append((nextNode[0],nextNode[1]+nowNode[1]))
	return deepNode

#입력
for _ in range(v):
#홀수번째는 Vertex 짝수번째는 간선의 가중치
	nodeinfo = list(map(int,stdin.readline().split()))
	leninfo = len(nodeinfo)
	for i in range(1,leninfo-1,2):
		if (nodeinfo[i],nodeinfo[i+1]) not in tree[nodeinfo[0]]:
			tree[nodeinfo[0]].append((nodeinfo[i],nodeinfo[i+1]))
		if (nodeinfo[0],nodeinfo[i+1]) not in tree[nodeinfo[i]]:
			tree[nodeinfo[i]].append((nodeinfo[0],nodeinfo[i+1]))
print(bfs(tree,bfs(tree,1)[0])[1])