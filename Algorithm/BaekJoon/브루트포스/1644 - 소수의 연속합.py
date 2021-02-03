def prime(n):
	sqn = int(n**0.5)
	pn = [False for _ in range(n+1)]
	pn[0],pn[1] = True,True
	for i in range(2,sqn):
		if not pn[i]:
			for j in range(i+i,n+1,i):
				pn[j] = True
	return [x for x in range(n+1) if not pn[x]]

n = int(input())

right,left,cnt,result = 0,0,0,0
nlist = prime(n)
nlen = len(nlist)
while True:
	if result >= n:
		result -= nlist[left]
		left += 1
	elif right == nlen:
		break
	else :
		result += nlist[right]
		right += 1
	if result == n:
		cnt += 1
print(cnt)