from sys import stdin
from collections import deque

gear = [deque([int(x) for x in stdin.readline().rstrip()]) for _ in range(4)]
c = int(stdin.readline())

#3시 방향 인덱스 = 2 / 9시 방향 인덱스 = 6

#왜 append(pop) 보다 rotate가 더 오래걸리는지 모르겠다.
def gearRotate(gnum,rnum):
	ro = -rnum
	rotateGear = []
	for i in range(1,4):
		if gear[i][6] == gear[i-1][2]:
			continue
		rotateGear.append(i)
	gear[gnum].rotate(rnum)
	
	for i in range(gnum+1,4):
		if i not in rotateGear:
			break
		gear[i].rotate(ro)
		ro *= -1

	ro = -rnum	
	for i in range(gnum-1,-1,-1):
		if i+1 not in rotateGear:
			break
		gear[i].rotate(ro)
		ro *= -1
for i in range(c):
	gearNum,rotate = map(int,stdin.readline().split())
	gearRotate(gearNum-1,rotate)

score = 0
for i in range(4):
	if gear[i][0] == 1:
		score += 2**i

print(score)