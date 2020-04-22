maps = [[0]*8 for _ in range(8)]
y= 6
x= 1

for i in range(1,8):
	if 0<=y-i<8:
		maps[y-i][x+i]=1
	else:
		break

for i in maps:
	print(i)
