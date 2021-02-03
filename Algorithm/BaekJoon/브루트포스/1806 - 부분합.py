from sys import stdin

#n - 길이 / s - 부분합
n , s = map(int,stdin.readline().split())
nlist = list(map(int,stdin.readline().split()))
right,left = 0,0
result = 0
ans = 100000

while True:
	if result >= s:
		result -= nlist[left]
		left += 1 
	elif right == n:
		if ans == 100000:
			print(0)
		else:
			print(ans)
		break
	else:
		result += nlist[right]
		right +=1
	if result >= s:
		ans = min(ans,right-left)