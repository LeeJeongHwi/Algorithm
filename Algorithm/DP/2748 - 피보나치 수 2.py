t = int(input())

memo = [-1 for _ in range(91)]
memo[0] = 0
memo[1] = 1

def fibo(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		if memo[n] != -1:
			return memo[n]
		memo[n] = fibo(n-1)+fibo(n-2)
		return memo[n]
fibo(t)
print(memo[t])