from sys import stdin

def gcd(a,b):
	if(b==0):
		return a
	else:
		return gcd(b,a%b)

def convert(num):
	return '1'*num


a,b = map(int,stdin.readline().split())
gn = gcd(a,b)

print(convert(gn))