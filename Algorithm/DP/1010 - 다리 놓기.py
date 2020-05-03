from sys import stdin

t = int(stdin.readline())

#nCr = n!/(n-r)!r!
for _ in range(t):
	r,n = map(int,stdin.readline().split())
	def facto(i):
		result = 1
		for f in range(i,0,-1):
			result*=f
		return result

	nf = facto(n)
	rf = facto(r)
	nrf = facto(n-r)
	print(int(nf/(nrf*rf)))
