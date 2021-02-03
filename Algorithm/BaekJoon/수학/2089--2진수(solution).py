n= int(input())
result = []
base = 1
if n ==0:
	print(0)
else:
	while n :
		if n%2 :
			result.append(1)
			n-=base
		else:
			result.append(0)
		base *= (-1)
		n//=2
		
for i in reversed(result):
	print(i,end='')