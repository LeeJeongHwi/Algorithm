n = int(input())
five,three = 0,0

five += n//5
n = n%5

while n!=0:
	if n%3 == 0 :
		three = n//3
		n%=3
	else:
		if five == 0 and n%3 != 0:
			break
		five -=1
		n+=5
	
if five==0 and n%3 != 0 : 
	print(-1)
else : 
	print(five+three)