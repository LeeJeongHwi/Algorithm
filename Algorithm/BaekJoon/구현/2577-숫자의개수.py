x=int(input())
y=int(input())
z=int(input())
nlist = [0]*10
re = str(x*y*z)
for i in re:
	nlist[int(i)]+=1
for i in nlist:
	print(i)
