n = int(input())

"""
각 대각선 배열의 합은 
1/1 == 2
1/2,2/1 == 3
3/1,2/2,1/3 == 4
1 3 6 10 15
 2 3 4  5  
14는 어디에 포함하는가?
"""
i=2
result = 1
while True:
	temp = result 
	result = result+i
	# print(temp,result)
	if temp<n<=result:
		count = n-temp
		# print(temp,result,i+1,count)
		c = 1
		if (i+1)%2==0:
			for j in range(0,i):
				if c == count:
					print(str(i-j)+'/'+str(j+1))
				c+=1
		else:
			for j in range(0,i):
				if c==count:
					print(str(j+1)+'/'+str(i-j))
				c+=1
		break
	i+=1
	