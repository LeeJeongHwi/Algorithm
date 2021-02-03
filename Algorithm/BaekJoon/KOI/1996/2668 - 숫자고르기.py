from sys import stdin

n = int(input())
nlist = [0]+[int(stdin.readline()) for _ in range(n)]
visit = [False for _ in range(n+1)]
result = []

def dfs(start):
	global result
	visit[start] = True
	cycle.append(start)
	next_vertex = nlist[start]

	if not visit[next_vertex]:
		dfs(next_vertex)
	else:
		if next_vertex in cycle:
			result += cycle[cycle.index(next_vertex):]
	return
for i in range(1,n+1):
	if not visit[i]:
		cycle = [] 
		dfs(i)
print(len(result))
result.sort()
for i in result:
	print(i)

# 1 2 3 4 5 6 7
# 2 6 5 4 3 2 7