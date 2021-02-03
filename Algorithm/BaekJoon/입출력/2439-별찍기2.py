# n = int(input())  내풀이

# for i in range(n):
# 	print(" "*(n-i-1),end='')
# 	print("*"*(i+1))

#백준 정답자 코드 
i = int(input())
j = 1
exec('print(" "*(i-j)+"*"*j);j+=1;'*i)
