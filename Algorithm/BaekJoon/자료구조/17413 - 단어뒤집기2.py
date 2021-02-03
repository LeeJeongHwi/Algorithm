from sys import stdin
strs = list(stdin.readline().rstrip())
strlen = len(strs)


def check_bracket(strs,idx):
	while strs[idx]!='>':
		print(strs[idx],end='')
		idx+=1
	print(strs[idx],end='')
	idx+=1
	return idx



idx = 0
st=[]
while idx!=strlen:
	if strs[idx] == '<':
		if st:
			while st:
				print(st.pop(),end='')
		idx = check_bracket(strs,idx)
		continue
	elif strs[idx] == ' ':
		if st:
			while st:
				print(st.pop(),end='')
		idx+=1
		print(' ',end='')
	st.append(strs[idx])
	idx+=1
if st:
	while st:
		print(st.pop(),end='')

#더 효율적인 풀이
s = ''
for t in input().split('<'):
	print(t)
	if '>' in t:
		x, y = t.split('>')
		print(x,y)
		s += '<' + x + '>' + ' '.join(map(lambda t: t[::-1], y.split(' ')))
	else: s += ' '.join(map(lambda t: t[::-1], t.split(' ')))
print(s)

