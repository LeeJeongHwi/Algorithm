from sys import stdin
from collections import deque
n,m,start = map(int,stdin.readline().split())

#입력값
graph = {}
for _ in range(m):
	a,b = map(int,stdin.readline().split())
	if a not in graph:
		graph[a] = [b]
	else:
		graph[a].append(b)

	if b not in graph:
		graph[b] = [a]
	else:
		graph[b].append(a)

#만약 시작지점에 연결된 노드들이 없다면 --> 런타임에러
for i in range(1,n+1): #런타임 에러 해결
	if i not in graph:
		graph[i] = []

def dfs(n,m,start):
	ans = []
	visit = [0 for _ in range(n+1)] #노드의 방문여부
	stack = [start]
	while stack:
		nowNode = stack.pop() #현재 있는 위치
		visit[nowNode]=1 #방문 했다는 표시!
		if nowNode not in ans: # 만약 답에 현재 방문한 노드 값이 없을 때
			ans.append(nowNode) # 답에 현재 방문한 노드를 추가
			nextNodes = sorted(graph[nowNode],reverse=True)
			#현재 방문한 노드에서 다음 방문한 노드들을 저장
			for node in nextNodes: #해당 노드들을 하나하나씩 검사
				if not visit[node]: #만약 다음 방문할 노드가 한번도 방문을 안했다면?
					stack.append(node) #stack에 node를 추가
	print(*ans)

#DFS와 다른 점은 Queue이냐 Stack이냐 차이
def bfs(n,m,start):
	ans = [] 
	visit = [0 for _ in range(n+1)]
	q = deque()
	q.append(start)
	visit[start]=1
	while q:
		nowNode = q.popleft()
		if nowNode not in ans:
			ans.append(nowNode)
			nextNodes = sorted(graph[nowNode])
			for node in nextNodes:
				if visit[node] == 0:
					visit[node] = 1
					q.append(node)
	print(*ans)
dfs(n,m,start)
bfs(n,m,start)