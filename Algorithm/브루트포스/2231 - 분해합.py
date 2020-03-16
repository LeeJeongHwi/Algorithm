from sys import stdin

n = stdin.readline().rstrip()

nlen = len(n)

ans = 1000001

con = int(n)-1

while con>0 :
	c = list(str(con))
	if con+sum(map(int,c)) == int(n):
		ans = min(con,ans)
	con-=1

if ans == 1000001:
	print(0)
else:
	print(ans)

	