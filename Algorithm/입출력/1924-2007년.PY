import calendar
from sys import stdin
day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
x,y = map(int,stdin.readline().split())
weekday = calendar.weekday(2007,x,y)

if weekday == 6:
	print(day[0])
else:
	print(day[weekday+1])