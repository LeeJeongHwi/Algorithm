from sys import stdin

for line in stdin:
	salpha = 0
	balpha = 0
	number = 0
	space = 0
	for i in line:
		if i >= 'a' and i <= 'z':
			salpha += 1
		elif i >= 'A' and i <= 'Z':
			balpha += 1
		elif i >= '0' and i <= '9':
			number += 1
		elif i == ' ':
			space += 1
		else:
			break
	print("{} {} {} {}".format(salpha,balpha,number,space))
