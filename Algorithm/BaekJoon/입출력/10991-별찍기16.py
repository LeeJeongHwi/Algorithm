n = int(input())
for i in range(1,n+1):
	print(' '*(n-i),end='')
	for j in range(2*i-1):
		if j % 2 :
			print(' ',end='')
		else:
			print("*",end='')
	print()

#다른사람 풀이
# n = int(input())
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*", end='')
#     print(" *" * (i - 1))