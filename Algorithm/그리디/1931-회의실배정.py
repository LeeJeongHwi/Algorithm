from sys import stdin

n = int(stdin.readline())

confer = []
for _ in range(n):
	confer.append(list(map(int,stdin.readline().split())))

confer.sort(key=lambda x: (x[1],x[0]) )

cnt = 1
now = confer[0]
for i in range(1,n):
	if now[1] <= confer[i][0]:
		now = confer[i]
		cnt +=1
print(cnt)

#힌트를 보고 풀었다!