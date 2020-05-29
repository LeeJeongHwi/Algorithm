from sys import stdin

class DisjointSet:
	def __init__(self,n):
		self.data = [-1]*n
		self.size = n
	def find_xy(self,x,y):
		x = self.find(x)
		y = self.find(y)
		if x == y:
			return True
		else:
			return False
	def find(self,index):
		value = self.data[index]
		if value < 0:
			return index
		return self.find(value)
	def union(self,x,y):
		x = self.find(x) #부모 찾기
		y = self.find(y) #부모 찾기

		if x == y:
			return 

		if self.data[x] > self.data[y]:
			self.data[x] = y
		elif self.data[x] < self.data[y]:
			self.data[y] = x
		else:
			self.data[x] -= 1
			self.data[y] = x
		self.size -=1

n = int(stdin.readline())
m = int(stdin.readline())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]
djs = DisjointSet(n)

for i in range(n):
	for j in range(n):
		if maps[i][j] == 1:
			djs.union(i,j)
plans = list(map(int,stdin.readline().split()))
for i in range(m-1):
	if djs.find_xy(plans[i]-1,plans[i+1]-1):
		continue
	else:
		print("NO")
		break
else:
	print("YES")
