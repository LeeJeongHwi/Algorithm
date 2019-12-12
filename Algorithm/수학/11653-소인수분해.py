from sys import stdin
n = int(stdin.readline())
if n==1:
	pass
else:
	while True:
		if n==1:
			break
		for i in range(2,n+1):
			if n%i == 0:
				n//=i
				print(i)
				break
