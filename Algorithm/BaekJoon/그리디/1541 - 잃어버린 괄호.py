from sys import stdin

exp = list(stdin.readline().rstrip().split('-'))

explen = len(exp)

result = 0

for i in range(explen):
	exp[i]=sum(list(map(int,exp[i].split('+'))))
	if i == 0:
		result += exp[i]
	else:
		result -= exp[i]
print(result)