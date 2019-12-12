from sys import stdin
s = stdin.readline().rstrip()
alpha = [-1] * 26
for i in range(len(s)):
	if alpha[ord(s[i])-97] == -1 :
		alpha[ord(s[i])-97]=i
print(" ".join(map(str,alpha)))

#다른사람 풀이

# s = input();print(*[s.find(chr(97+i)) for i in range(26)])