#난 진짜 분할정복에 존나 약하구나;
#solution : https://jaemin8852.tistory.com/251
import sys
sys.setrecursionlimit(10**9)
N,r,c = map(int,input().split())

# result = 0
# flag = False
# def solve(y,x,n):
# 	global result,flag
# 	if (y==r and x==c):
# 		flag = True
# 		return result
# 	if not flag:
# 		if n == 1:
# 			result+=1
# 			return
# 		if not (y<=r<y+n and x<=c<x+n): #포함되지 않은 사분면
# 			result += n**2
# 			return
# 	else:
# 		return
# 	solve(y,x,n//2)
# 	solve(y,x+(n//2),n//2)
# 	solve(y+(n//2),x,n//2)
# 	solve(y+(n//2),x+(n//2),n//2)

# solve(0,0,2**N)
# print(result)

def solve(n,r,c):
	ans = 0
	while(n):
		s = pow(2,n)//2
		if (c<s and r<s): # 4시분면
			idx = 0
		elif (c>=s and r<s): #1사분면
			idx = 1
		elif (c<s and r>=s): #3사분면
			idx = 2
		elif (c>=s and r>=s): #2사분면
			idx = 3
		r%=s
		c%=s
		ans += pow(s,2) * idx #사분면 갯수
		# 1사분면이면 +4
		# 2사분면이면 +12
		# 3사분면이면 +8
		# 4사분면이면 +0
		n-=1
	print(ans)
solve(N,r,c)





