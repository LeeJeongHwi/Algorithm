num = int(input())

def binaryTile(n):
	last2 = 1
	last = 2
	for i in range(3, n+1):
		last2 , last = last%15746 , (last2+last) % 15746
	print(last)

binaryTile(num)