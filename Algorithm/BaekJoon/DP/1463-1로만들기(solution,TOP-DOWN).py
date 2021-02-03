#TOP-DOWN 방법(BOJ에서는 메모리초과가 난다)
import sys
sys.setrecursionlimit(10**6+1)

def f(n): 
	if n == 1 : 
		return 0
	if dp[n] != -1 : 
		return dp[n]

	result = f(n-1) + 1
	
	if n%3 == 0 :
		result = min(result,f(n//3)+1)
	if n%2 == 0 :
		result = min(result,f(n//2)+1)
	
	dp[n] = result
	return result

if __name__ == "__main__":
	i = int(input())
	dp = [-1]*(i+1)
	print(f(i))