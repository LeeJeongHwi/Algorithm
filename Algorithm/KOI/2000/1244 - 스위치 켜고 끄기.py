from sys import stdin

n = int(stdin.readline())
switch = [0] + list(map(int,stdin.readline().split()))
tc = int(stdin.readline())

def change_Switch(mf,s):
	if mf == 1: #남자인 경우
		for i in range(s,n+1,s):
			switch[i] = 0 if switch[i] else 1
		# print(switch[1:])
	elif mf == 2: #여자인 경우
		if 1<=s-1 and s+1<=n: 
			if switch[s-1] != switch[s+1]:
				switch[s] = 0 if switch[s] else 1
			else:
				i=1
				switch[s] = 0 if switch[s] else 1
				while True:
					if 1<=s-i and s+i<=n:
						if switch[s-i] != switch[s+i]:
							break
						switch[s-i] = 0 if switch[s-i] else 1
						switch[s+i] = 0 if switch[s+i] else 1
						i+=1
					else:
						break
		else:
			switch[s] = 0 if switch[s] else 1
		# print(switch[1:])
for _ in range(tc):
	mf,selected_Switch = map(int,stdin.readline().split())
	change_Switch(mf,selected_Switch)

i=1
while i<=n:
	if i%20 == 0:
		print("{:d}".format(switch[i]))
	else:
		print("{:d}".format(switch[i]),end=' ')
	i+=1