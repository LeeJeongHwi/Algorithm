"""
시간 : 60ms
"""
x = int(input())

stick = [64]

while True:
	if sum(stick) == x:
		print(len(stick))
		break
	if sum(stick) > x:			
		s = stick.pop()//2
		r = s
		if r+sum(stick) >= x:
			r = 0
			stick.append(s)
		else:
			stick.append(s)
			stick.append(r)

# 시간 : 56 ms
print(bin(int(input())).count('1'))