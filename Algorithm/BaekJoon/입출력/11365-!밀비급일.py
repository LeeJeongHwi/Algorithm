from sys import stdin

while True:
	try:
		S = stdin.readline().rstrip()
		if(S == "END"):
			break
		else:
			print(''.join(reversed(S)))
	except EOFError:
		break

#try-except 구문이 없어 질 시 시간이 더 늘고 (시간 : 64ms)
#있을 시 코드 길이가 길어짐 (시간 : 56ms)