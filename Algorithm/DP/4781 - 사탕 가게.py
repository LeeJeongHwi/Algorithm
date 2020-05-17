from sys import stdin

#----------------------------------Solve
def solve(dp):
	for i in range(1,n+1):
		for j in range(price[i],m+1):
			dp[j] = max(dp[j],dp[j-price[i]]+kcal[i])
		# print(dp)
#----------------------------------init
while True:
	n,m = map(float,stdin.readline().split())
	n=int(n)
	if n ==0 and m == 0.00:
		break
	m=int(m*100)
	dp = [0]*(m+1)
	kcal = [0]
	price = [0]
	for i in range(n):
		c,p = map(float,stdin.readline().split())
		c=int(c) ; p = int(p*100+0.5)
		kcal.append(c)
		price.append(p)
	# print(kcal,price)
	solve(dp)
	print(dp[m])