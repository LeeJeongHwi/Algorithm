# 1~99 까지는 무조건 포함
# 3자리수부터 걸러짐
from sys import stdin
n = stdin.readline()
count = 0
#1,2자리 수 일 때
if int(n) < 100:
 	print(int(n))	
#3자리,4자리일 때
elif int(n) >= 100:
	count += 99
	for i in range(100,int(n)+1):
		i = str(i)
		if (int(i[1])-int(i[0]) == (int(i[2])-int(i[1]))):
			count+=1
	print(count)