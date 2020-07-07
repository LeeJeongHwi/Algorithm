"""
YXX YYXX 형태
걷는 거리가 같을 때에는 아래층의 방을 더 선호
102호 보다는 301호 ==> 걷는 시간이 더 짧기 때문
"""
from sys import stdin
import math
t = int(input())

for _ in range(t):
	h,w,n = map(int,stdin.readline().split())
	floor = n%h
	if not floor:
		floor = h
	room_number = math.ceil(n/h)
	if room_number <10:
		print("{:0d}0{:0d}".format(floor,room_number))
	else:
		print("{:0d}{:0d}".format(floor,room_number))

