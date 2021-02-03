#Top-Down
def f(n):
	if n<5:
		return memo[n]
	else:
		if memo[n] != -1 :
			return memo[n]
		else: 
			memo[n]= f(n-3)+f(n-2)+f(n-1)
			return memo[n]
if __name__ == "__main__":
	T = int(input())
	memo = [-1] * 12
	memo[1] = 1
	memo[2] = 2
	memo[3] = 4
	memo[4] = 7
	for i in range(T):
		n=int(input())
		print(f(n))