#재귀문제이다. 정확히 공부하자 
#solution : https://hon6036.github.io/%EB%B6%84%ED%95%A0%20%EC%A0%95%EB%B3%B5/1629/
#pow(a,b,c) 로도 풀 수 있다.
a,b,c = map(int,input().split())

def power(a,b):
	if b == 0:
		return 1
	elif b == 1:
		return a
	else:
		if b%2 == 0:
			temp = power(a,b//2)
			# print("before % :",temp)
			temp %= c           #이부분
			# print("After % :",temp)
			return temp**2 %c   #이부분 이해가 안됨
		elif b%2 == 1:
			return power(a,b-1)*a
print(power(a,b)%c)