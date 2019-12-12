#Top-Down
import sys
sys.setrecursionlimit(1001)
def f(n) : 
	if n < 3:
		return n
	if memo[n] != -1 :
		return memo[n]

	memo[n] = f(n-2) + f(n-1) # BOJ에서는 이렇게 표현하자;
	return memo[n]

if __name__=="__main__":
	n=int(input())
	memo = [-1]*(n+1)
	print(f(n)%10007)