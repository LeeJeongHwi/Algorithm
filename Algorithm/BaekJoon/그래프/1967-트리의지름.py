"""
Solution : https://qkqhxla1.tistory.com/748
"""
from collections import deque
from sys import stdin
#가중치의 Dict와 Tree의 dict를 다르게쓰는건 어떨까? ->안돼 멍청아
n = int(stdin.readline())
tree = [[] for _ in range(n+1)] #자식이 있는 부모 노드정보

def bfs(tree,start): # 가장 깊은 노드 중 가중치가 큰 노드를 찾기
	visit = [0 for _ in range(n+1)]
	queue = deque()
	queue.append((start,0))
	visit[start] = 1
	deepNode = [start,0]
	while queue:
		node = queue.popleft() #tuple형식의 노드 node[0] = NodeNumber , node[1] = NodeWeight
		if node[1] > deepNode[1]:
				deepNode = node
		for nextNode in tree[node[0]]: #nextNode = (Next_NodeNumber, NodeWeight)
			if not visit[nextNode[0]]:
				visit[nextNode[0]] = 1
				queue.append((nextNode[0],nextNode[1]+node[1]))
			
	return deepNode

for _ in range(n-1):
	nowNode,nextNode,nodeWieght = map(int,stdin.readline().split())
	tree[nowNode].append((nextNode,nodeWieght))
	tree[nextNode].append((nowNode,nodeWieght))
#가장 깊은 노드 중 가중치가 가장 큰 것
deepNode = bfs(tree,1)
#그 깊은 노드 중 가중치가 큰 것을 다시 찾기
print(bfs(tree,deepNode[0])[1])