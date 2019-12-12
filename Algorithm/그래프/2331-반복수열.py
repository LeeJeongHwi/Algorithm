from sys import stdin

first_repeat = -1
last_repeat = -1

def calc(a,p,result):
	sa = str(a)
	re = 0
	for i in sa:
		re += int(i)**p
	if re in result:
		global first_repeat
		global last_repeat
		first_repeat = result.index(re)
		last_repeat = len(result)-1
		return
	else:	
		result.append(re)
		calc(re,p,result)

if __name__ == '__main__':
	A,P = map(int,stdin.readline().split())
	result = []
	result.append(A)
	calc(A,P,result)

	setre = result[first_repeat:last_repeat+1]
	print(len(set(result)-set(setre)))