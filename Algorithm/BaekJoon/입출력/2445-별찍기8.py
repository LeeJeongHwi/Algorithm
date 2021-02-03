T = int(input())
for i in range(1,T+1):
	print("*"*i,end='')
	print(" "*(2*(T-i)),end='')
	print("*"*i)
for i in range(T-1,0,-1):
	print("*"*i,end='')
	print(" "*(2*(T-i)),end='')
	print("*"*i)