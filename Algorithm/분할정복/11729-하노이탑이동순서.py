n = int(input())

movement = []
def hanoi(num,froms,to,by):
	global cnt
	if num>0:
		hanoi(num-1,froms,by,to)
		print(froms,to)
		hanoi(num-1,by,to,froms)
print(pow(2,n)-1)
hanoi(n,1,3,2)