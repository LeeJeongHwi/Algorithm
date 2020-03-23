from sys import stdin

train = [list(map(int,stdin.readline().split())) for _ in range(4)]

 # (내린 사람, 탄 사람 )

maxPeople = 0
remain = train[0][1]
for i in range(1,4):
	remain = remain-train[i][0] + train[i][1]
	maxPeople = max(maxPeople,remain)
print(maxPeople)