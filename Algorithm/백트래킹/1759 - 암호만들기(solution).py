"""
Solution : https://www.crocus.co.kr/705
"""
from sys import stdin

l , c = map(int,stdin.readline().split())
strlist = stdin.readline().split()

def backtracking(string , i , ja, mo):
	if len(string) == l:
		if ja < 2 or mo < 1:
			return
		print(string)

	for j in range(i,c):
		if strlist[j] in ['a','e','i','o','u']:
			backtracking(string+strlist[j],j+1,ja,mo+1)
		else:
			backtracking(string+strlist[j],j+1,ja+1,mo)

strlist.sort()
backtracking("",0,0,0)


"""
56ms 307Byte
L, C = map(int, input().split())
from itertools import combinations as cm
def count(s):
    c = 0
    for i in s:
        if i in 'aeiou':
            c += 1
    return c > 0 and len(s) - c > 1
s = sorted(input().split())
cnt = 0
for t in cm(s, L):
    tmp = ''.join(t)
    if count(tmp):
        print(tmp)
"""