#Bottom - Up
n = int(input())

memo = [-1]*(n+1)
memo[0] = 0

for i in range (1,n+1):
	if i == 1:
		memo[1] = 1
	elif i ==2 :
		memo[2] = 3
	else:
		memo[i] = (2*memo[i-2])+memo[i-1]

print(memo[n]%10007)