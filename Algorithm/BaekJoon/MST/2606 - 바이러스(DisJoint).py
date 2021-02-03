from sys import stdin

def union(x,y):
	x,y = find(x),find(y)
	if x!=y:
		network[y] = x
def find(x):
	if network[x] < 0:
		return x
	network[x] = find(network[x])
	return network[x]

c = int(input())
r = int(input())

network = [0]+[-1 for _ in range(c)]
for _ in range(r):
	a,b = map(int,stdin.readline().split())
	union(a,b)
count = 0
for i in range(2,c+1):
	if find(1) == find(i):
		count +=1
# print(network)
print(count)