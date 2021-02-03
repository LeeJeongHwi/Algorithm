"""

a : 97 , z:122
A : 65 , Z:90

+ascii코드에서 +13 한 값들을 출력

"""
from sys import stdin

st = stdin.readline().rstrip()
for i in st:
	if i >= 'a' and i<='z':
		if ord(i)+13 <= 122:
			print(chr(ord(i)+13),end='')
		else:
			print(chr((ord(i)+13)-26),end='')
	elif i >= 'A' and i<='Z':
		if ord(i)+13 <= 90:
			print(chr(ord(i)+13),end='')
		else:
			print(chr((ord(i)+13)-26),end='')
	else:
		print(i,end='')
		