hour,minute=map(int,input().split())
if minute-45 < 0:
	hour -=1
	minute = 60 + (minute-45)
	print(hour%24,minute)
else:
	print(hour,minute-45)