from sys import stdin

n = int(stdin.readline())
c = int(stdin.readline())

network = [[]*(n+1) for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
for _ in range(c):
	f,s = map(int,stdin.readline().split())
	network[f].append(s)
	network[s].append(f)

def dfs(start,visit):
	for nextNode in network[start]:
		if visit[nextNode] == 0:
			visit[nextNode] = 1
			dfs(nextNode,visit)
dfs(1,visit)
print(sum(visit) -1)