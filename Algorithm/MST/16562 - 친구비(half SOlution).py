#half solution : https://akim9905.tistory.com/22
from sys import stdin,setrecursionlimit
setrecursionlimit(10**8)
n,m,k = map(int,stdin.readline().split())

price = list(map(int,stdin.readline().split()))

friends = [-1 for _ in range(n)]

def find(index):
	global friends
	if(friends[index] < 0):
		return index
	friends[index] = find(friends[index])
	return friends[index]

def union(x,y):
	global friends
	x = find(x)
	y = find(y)
	if x==y:
		return
	if price[x] < price[y]:
		friends[y] = x
	else:
		friends[x] = y;
#Union
for _ in range(m):
	x,y = map(int,stdin.readline().split())
	union(x-1,y-1)
result = 0
# print(friends)
for i in range(n):
	if friends[i]< 0:
		result+=price[i]
if result<=k: print(result)
else: print("Oh no")