from sys import stdin

n = int(stdin.readline())
re=1
if n == 0:
	pass
else:
	for i in range(1,n+1):
		re*=i
re=str(re)
count=0
re=list(reversed(re))
for i in re:
	if i == '0':
		count+=1
	else:
		break
print(count)