# 
# A B C D E F G H I J K L N M O P Q R S T U V W X Y Z
#
from sys import stdin
n = stdin.readline().rstrip()
ar = [int(x) for x in n]
arr_len = len(ar)
dp = [0] * (arr_len+1)
dp[0] = 1
for i in range(1,arr_len+1):
	if ar[i-1] >= 1 and ar[i-1] <= 9:
		dp[i] += dp[i-1]
	if i == 1 : 
		continue

	if (ar[i-2]*10 + ar[i-1]) >= 10 and (ar[i-2]*10 + ar[i-1]) <=26:
		dp[i] += dp[i-2]
print(dp[arr_len] % 1000000)
