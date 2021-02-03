from sys import stdin

maps = [[0 for _ in range(101)] for _ in range(101)]

count = 0
for _ in range(4):
	x1,y1,x2,y2 = map(int,stdin.readline().split())
	for y in range(y1,y2):
		for x in range(x1,x2):
			if not maps[y][x]:
				count+=1
				maps[y][x] = 1
print(count)