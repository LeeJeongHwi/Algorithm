from sys import stdin

line = stdin.readline().rstrip()
substr = []
ilen = len(line)
for i in range(ilen):
	substr.append(line[i:])

for i in sorted(substr):
	print(i)