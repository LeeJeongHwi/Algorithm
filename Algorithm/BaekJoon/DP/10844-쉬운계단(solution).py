#Top - Down
#row는 행 col은 열

n= int(input())

dp = [[1 for col in range(11)] for row in range(101)]
#dp[n][l] = dp[n-1][l-1] + dp[n-1][n+1] 이렇게 이루어져 있다.
# but 이 점화식은 l이 1~8일때만 해당
# n=1 -> l은 0이 될수 없다.
# n=2 -> 9뒤에는 only 8만 가능
# l = 0 일때 dp[n][0] = dp[n-1][l+1]
# l = 9 일때 dp[n][9] = dp[n-1][l-1]
for i in range(2,n+1):
	for j in range(10):
		if j==0:
			dp[i][j] = dp[i-1][j+1]
		elif j == 9 :
			dp[i][j] = dp[i-1][j-1]
		else:
			dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]
sum =0
for i in range(1,10):
	sum += dp[n][i]

print(sum%1000000000)


for i in range(n+1):
	print(dp[i][0:10])