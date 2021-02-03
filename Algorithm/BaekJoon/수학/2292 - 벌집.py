n = int(input())
#1 과 n 사이의 층을 계산
"""
1 - 7 - 19 - 37 - 61
  6   12   18   24   ...
"""
i=0
result = 1
while True:
	if n == 1:
		print(1)
		break
	temp = result
	result = result+(6*i)
	if temp<n<=result:
		print(i+1)
		break
	i+=1