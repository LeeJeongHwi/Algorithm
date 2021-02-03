from sys import stdin
n,m = map(int,stdin.readline().split())

# 0 union 1 find
class DisjointSet:
	def __init__(self,n):
		self.data = [-1 for _ in range(n)]
		self.size = n

	def find_as(self,x,y):
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
		x = self.find(x)
		y = self.find(y)

		if x == y:
			return

		if self.data[x] < self.data[y]:
			self.data[y] = x
		elif self.data[x] > self.data[y]:
			self.data[x] = y
		else:
			self.data[x] -=1
			self.data[y] = x
		self.size -= 1

disjoint = DisjointSet(n+1)

for _ in range(m):
	ins,x,y = map(int,stdin.readline().split())
	if ins == 0:
		disjoint.union(x,y)
	elif ins == 1:
		if disjoint.find_as(x,y)
			print("YES")
		else:
			print("NO")
	# print(disjoint.data)