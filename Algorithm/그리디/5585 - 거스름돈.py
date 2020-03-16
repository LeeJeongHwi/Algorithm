n = int(input())

remain = 1000-n

count = 0

def pay(money):
	global remain,count
	count +=1
	remain -= money
	if remain < 0:
		count -=1
		remain += money
		return False
	else:
		return True

while remain!=0:
	for i in [500,100,50,10,5,1]:
		if pay(i):
			break

print(count)